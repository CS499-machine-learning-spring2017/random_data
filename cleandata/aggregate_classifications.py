#!/usr/bin/env python
'''
Purpose: Aggregate the classifications in the alpha files
    so the data isn't skewed towards one type
'''
import sys
import csv
import json
from os import path
from collections import Counter

def getHardCodedFiles():
    folder = "data_small"
    tmpfile = folder + "/" +"cleaned_{}.alpha"
    files = [tmpfile.format(i) for i in [1, 2, 13, 45]]
    return files

def aggregate(file):
    height, width = 0, 0
    counter = Counter()
    with open(file, "r") as infile:
        reader = csv.reader(infile)
        first = next(reader)
        width = len(first)
        counter.update(first)
        height += 1
        for row in reader:
            height += 1
            counter.update(row)
    return {"height":height, "width": width, "info":dict(counter)}

def aggregateFiles(file):
    if path.isfile(file):
        return aggregate(file)
    else:
        print "Couldn't find file {}".format(file)

def main():
    files = getHardCodedFiles()
    data = {}
    for file in files:
        data[file] = aggregateFiles(file)
    return json.dumps(data)

if __name__ == "__main__":
    print main()
