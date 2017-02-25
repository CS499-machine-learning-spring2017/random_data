#!/usr/bin/env python
from random import randrange
from sys import stdout, exit, argv

'''
To run:
    python movingwindow <windowsize> <rows of data>

Purpose:
    This program will generate random data given a specified window
    and will take a specified number for rows
'''


class RandomData:
    '''Generates random data to replicate what our test data will be
        returns the row and the average of the row
        accepts a window size and how many lines of data you want'''

    maxnum = 256

    def __init__(self, window, linenums):
        '''
        window: represents the horizontal ad vertical length of data for the window
        maxrow: max length of the generated row to save space
        linesnums: how many lines of data to generate
        rows = contains rows of data
        curindex: current index to generate window data from
        '''
        self.window = window
        self.maxrow = (2 * self.window) - 1
        self.linenums = linenums
        self.rows = []
        self.curindex = 0

    def makerows(self):
        '''make rows of random data'''
        return [ randrange(self.maxnum) for _ in range(self.maxrow)]

    def _initrows(self):
        '''initialize all rows to start generating rows'''
        for _ in range(self.window):
           self.rows.append(self.makerows())

    def average(self, row):
        '''take the average of the given row and returns a float'''
        return ((float(sum(row)) / len(row)))

    def _cleanupindex(self):
        '''function to handle generating new rows of data'''
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
        flattenrow = [item for row in newrow for item in row]
        self._cleanupindex()
        return (flattenrow, self.average(flattenrow))

    def getdata(self):
        '''returns rows of data'''
        self._initrows()
        for _ in range(self.linenums):
            yield self._gendata()

def main():
    '''only here for testing, but returns data in a csv format'''
    randdata = RandomData(window = int(argv[1]), linenums = int(argv[2]))
    for dataitem in randdata.getdata():
        row, average = dataitem
        row = map(str, row)
        stdout.write("{},{}\n".format(','.join(row), average))
        stdout.flush()

if __name__ == '__main__':
    main()
