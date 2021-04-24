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
        if parsed.message_type != protocol.RESPONSE:
            print("<<<", parsed)
            return

        msg_id = parsed.response.cmd_id
        result = parsed.response.response_code
        async with self.process_lock:
            try:
                waiter = self.in_process[msg_id]
            except KeyError:
                self.in_process[msg_id] = result_waiter(result)
                return

        waiter.set(result)
        await waiter.received()

    async def get_reponse(self, msg_id):
        async with self.process_lock:
            try:
                return self.in_process.pop(msg_id).result
            except KeyError:
                waiter = result_waiter()
                self.in_process[msg_id] = waiter

        return await waiter.get()
