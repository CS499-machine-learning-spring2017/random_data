#!/usr/bin/env python
from random import randrange
from sys import stdout, exit

'''
This program will generate random data given a specified window
and will take a specified number for rows
'''


class RandomData:

    maxnum = 256

    def __init__(self, window, linenums):
        self.window = window
        self.maxrow = (2 * self.window) - 1
        self.linenums = linenums
        self.rows = []
        self.curindex = 0

    def makerows(self):
        return [ randrange(self.maxnum) for _ in range((self.window * 2) - 1)]

    def _initrows(self):
        for _ in range(self.window):
           self.rows.append(self.makerows())

    def average(self, row):
        return ((float(sum(row)) / len(row)))

    def _cleanupindex(self):
        self.curindex += 1
        if self.curindex >= self.window:
            self.curindex = 0
            self.rows.pop(0)
            self.rows.append(self.makerows())

    def _gendata(self):
        '''This will generate data to be returned will have to take a window size of
            every row in rows join them to a single list, take the average
            and return a tuple of it'''
        for row in self.rows: print row
        newrow = [row[self.curindex: self.curindex + self.window] for row in self.rows ]
        print newrow
        flattenrow = [item for row in newrow for item in row]
        print flattenrow
        print ''
        self._cleanupindex()
        return (flattenrow, self.average(flattenrow))

    def getdata(self):
        self._initrows()
        for _ in range(self.linenums):
            yield self._gendata()

def main():
    x = RandomData(window = 5, linenums = 10)
    counter = 1
    for dataitem in x.getdata():
        row, average = dataitem
        stdout.write("\rData entry #{}: {} with averge = {}, len(row) = {}\n".format(counter,row, average, len(row)))
        stdout.flush()
        counter += 1

if __name__ == '__main__':
    main()
