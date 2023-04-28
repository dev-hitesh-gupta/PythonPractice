import asyncio


async def get_some_values_from_io():
    await asyncio.sleep(2)
    return [1, 2, 3, 4, 5, 6, 8, 7]


vals = []


async def fetcher():
    while True:
        io_vals = await get_some_values_from_io()

        for val in io_vals:
            vals.append(io_vals)


async def monitor():
    while True:
        print(len(vals))

        await asyncio.sleep(1)


async def main():
    await asyncio.gather(fetcher(), monitor())


asyncio.run(main())
