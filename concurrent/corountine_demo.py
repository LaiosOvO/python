
import asyncio
from utils import async_timed

@async_timed
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


if __name__ == '__main__':
    coro = main()
    asyncio.run(coro)