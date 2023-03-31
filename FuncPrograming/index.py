import csv
from itertools import groupby


# Use itertools and functools to group by data using 2nd column
def keyfunc(row):
    return row[1]

def groupbyKey(data, key=None):
    groups = []
    uniquekeys = []
    data = sorted(data, key=keyfunc)
    for k, g in groupby(data, keyfunc):
        groups.append(list(g))
        uniquekeys.append(k)
    return groups, uniquekeys

def main():
    print('Grouping by 2nd column')
    with open('sample.csv') as f:
        reader = csv.reader(f)
        data = list(reader)
        groups, uniquekeys = groupbyKey(data, keyfunc)
        print(groups[1])

if __name__ == '__main__':
    main()

