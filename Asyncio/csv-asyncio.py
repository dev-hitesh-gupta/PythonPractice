import asyncio
import csv
import time

start = time.time()


async def process_csv():
    with open('sample.csv', newline='') as readFile, open('output.csv', "w+") as writeFile:
        reader = csv.reader(readFile)
        writer = csv.writer(writeFile)
        for row in reader:
            await write_csv(writer, row)


async def write_csv(writer, row):
    writer.writerow(row)


asyncio.run(process_csv())
end = time.time()
print(end - start)
