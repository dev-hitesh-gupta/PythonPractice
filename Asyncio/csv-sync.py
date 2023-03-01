import csv
import time

start = time.time()

def write_csv(writer, row):
    writer.writerow(row)

def process_csv():
    with open('sample.csv', newline='') as readFile, open('output.csv', "w+") as writeFile:
        reader = csv.reader(readFile)
        writer = csv.writer(writeFile)
        for row in reader:
            write_csv(writer,row)



process_csv()
end = time.time()
print(end - start)