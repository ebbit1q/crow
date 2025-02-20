import asyncio

from . import protocol

MAX_TIMEOUT = 10  # seconds


class result_waiter:
    def __init__(self, result=None):
        self.result = result
        self.dummy = result is not None
        if result is None:
            self._get = asyncio.Event()
            self._received = asyncio.Event()

    def set(self, result):
        self.result = result
        self._get.set()

    async def get(self):
        await asyncio.wait_for(self._get.wait(), MAX_TIMEOUT)
        self._received.set()
        return self.result

    async def received(self):
        await asyncio.wait_for(self._received.wait(), MAX_TIMEOUT)

    def __repr__(self):
        base = f"{self.__class__.__name__}({self.result})"
        if self.dummy:
            return base

        if self._get.is_set():
            return f"{base} gotten"
        elif self._received.is_set():
            return f"{base} received"
        else:
            return f"{base} waiting"


class handler:
    def __init__(self):
        self.process_lock = asyncio.Lock()
        self.in_process = {}

    async def handle(self, message):
        parsed = protocol.parse_server_message(message)
        if parsed.message_type == protocol.SERVER_RESPONSE:
            await self.handle_response(parsed.response)
        elif parsed.message_type == protocol.SESSION_EVENT:
            print("received event:")
            print(parsed.session_event)
        elif parsed.message_type == protocol.GAME_EVENT_CONTAINER:
            print("received room events:")
            for event in parsed.game_event_container.event_list:
                print(event)
        elif parsed.message_type == protocol.ROOM_EVENT:
            print("received room event:")
            print(parsed.room_event)
        else:
            print("received unrecognized message from server:")
            print(parsed)

    async def handle_response(self, response):
        msg_id = response.cmd_id
        result = response
        async with self.process_lock:
            try:
                waiter = self.in_process[msg_id]
            except KeyError:
                self.in_process[msg_id] = result_waiter(result)
                return

        waiter.set(result)
        try:
            await waiter.received()
        finally:
            async with self.process_lock:
                self.in_process.pop(msg_id)

    async def get_response(self, msg_id):
        async with self.process_lock:
            try:
                return self.in_process.pop(msg_id).result
            except KeyError:
                waiter = result_waiter()
                self.in_process[msg_id] = waiter

        return await waiter.get()
