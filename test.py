import asyncio

from . import crow

# note that each connection takes one thread, default ulimit -n is 1024
USERS = 1000
URL = "ws://localhost:4748"


async def main():
    items = [crow(URL, f"user{i}") for i in range(USERS)]
    await asyncio.gather(*[item.login() for item in items])
    await asyncio.sleep(3)
    await asyncio.gather(*[item.stop() for item in items])


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if args:
        USERS = int(args[0])

    asyncio.run(main(), debug=True)
