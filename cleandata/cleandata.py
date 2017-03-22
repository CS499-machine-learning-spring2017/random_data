#!/usr/bin/env python
import sys

def getdemensions(data):
    data = data.strip().split(" ")
    data = map(int, data)
    return data

def cleandata(data):
    data = data.replace("\xff", "")
    cleaneddata = [ord(d) for d in data]
    print "Here is a segment of the cleaned data"
    print cleaneddata[0: 50]
    return cleaneddata

def getrows(data, width):
    for pos in range(0, len(data), width):
        yield data[pos: pos + width]

def writefile(filename, data, width):
    cleaneddata = cleandata(data)
    with open("cleaned_" + filename, "wb") as outfile:
        for row in getrows(cleaneddata, width):
            rowstr = map(str, row)
            newrow = ",".join(rowstr) + "\n"
            outfile.write(newrow)

def cleanfile(file):
    try:
        infile = open(file, "rb")
    except:
        raise Exception("File doesn't exits")

    width, _ = getdemensions(infile.readline())
    data = infile.read()
    writefile(file, data, width)

if __name__ == "__main__":
    files = sys.argv[1:]
    map(cleanfile, files)
