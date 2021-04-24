import asyncio
import websockets

from asyncio.exceptions import TimeoutError
from asyncio.exceptions import CancelledError


class connection:
    def __init__(self, handler):
        self.handler = handler

    async def ask(self):
        print("SOCK IS OPEN")
        try:
            while self.sock.open:
                got = await self.sock.recv()
                asyncio.create_task(self.handler.handle(got))
        except CancelledError:
            await self.sock.close()
            print("SOCK HAS CLOSED")

    async def connect(self, url):
        self.sock = await websockets.connect(url)
        self.loop = asyncio.create_task(self.ask())

    async def send(self, *args, **kwargs):
        return await self.sock.send(*args, **kwargs)

    def close(self):
        self.loop.cancel()
