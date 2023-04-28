import asyncio
import time

import aiofiles as aiofiles

start = time.time()
lines = []
fileReadGoing = True


async def read_csv():
    global fileReadGoing
    async with aiofiles.open('sample.csv') as f:
        async for line in f:
            lines.append(line)
    fileReadGoing = False


async def write_csv():
    async with aiofiles.open('output.csv', "w+") as f:
        while fileReadGoing:
            print(lines)
            while len(lines) > 0:
                await f.write(lines.pop())
            await asyncio.sleep(0)


async def main():
    await asyncio.gather(read_csv(), write_csv())


asyncio.run(main())
end = time.time()
print(end - start)
