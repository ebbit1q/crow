import asyncio
import websockets

from asyncio.exceptions import CancelledError
from websockets.exceptions import ConnectionClosedOK


class connection:
    def __init__(self, handler):
        self.handler = handler

    async def ask(self):
        print("SOCK IS OPEN")
        try:
            while self.sock.state is websockets.State.OPEN:
                got = await self.sock.recv()
                asyncio.create_task(self.handler.handle(got))
        except CancelledError:
            await self.sock.close()
            print("SOCK HAS CLOSED")
        except ConnectionClosedOK:
            print("SERVER CLOSED CONNECTION")

    async def connect(self, url):
        self.sock = await websockets.connect(url)
        self.loop = asyncio.create_task(self.ask())

    async def send(self, *args, **kwargs):
        return await self.sock.send(*args, **kwargs)

    def close(self):
        self.loop.cancel()
