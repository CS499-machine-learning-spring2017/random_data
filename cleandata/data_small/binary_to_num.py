#!/usr/bin/env python
from os import path
from sys import argv, stdout

def readfile(file):
    with open(file, "rb") as infile:
        with open("dec_"+file, "w") as outfile:
            counter = 1
            for line in infile:
                try:
                    newline = line.decode('hex')
                    outfile.write(newline)
                    stdout.write('\rWriting line {}'.format(counter))
                    stdout.flush()
                except:
                    pass

def main(filename):
    if path.isfile(filename):
        readfile(filename)
    else:
        raise Exception("Couldn't find file")

if __name__ == '__main__':
    if len(argv) != 2:
        print "Need a file to decode"
    else:
        main(argv[1])
