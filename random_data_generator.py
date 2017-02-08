#!/usr/bin/python
import sys, csv
from random import randrange
from copy import deepcopy

def setdata(linenum, window, setnum):
	for _ in range(linenum):
		yield [setnum for _ in range(window)]

def sequentialdata(linenum, windowsize):
	'''Produces lines that will sequentially decrease
		The first line will be [255] * windowsize and
		decrease all the way to [0] * windowsize'''
	decrementor = max(int(linenum  / windowsize), 1)
	previousrow = [255] * windowsize
	maxrow = 1
	for _ in range(linenum + 1):
		yield previousrow
		newrow = deepcopy(previousrow)
		for i in range(maxrow):
			newrow[i] = int(max(newrow[i] - decrementor, 0))
		if maxrow < windowsize:
			maxrow += 1

def randomdata(linenum, windowsize):
	for _ in range(linenum):
		yield [ randrange(256) for _ in range(windowsize)]

def randdatagenerator(filename, linenum, window, datatype, setnum = 0):
	''' Generate the random numbers for  '''
	if datatype == 'set':
		gen = setdata(linenum, window, setnum)
	elif datatype == 'sequential':
		gen =sequentialdata(linenum, window)
	else:
		gen = randomdata(linenum, window)
	
	with open(filename, 'w') as outfile:
		writer = csv.writer(outfile)
		for line in gen:
			writer.writerow(line)

if __name__ == '__main__':
	print "This generates random data"
	print "\t-f <filename>.csv (This will generate a csv)"
	print "\t-n <num> (How many rows of data do you want?)"
	print "\t-w <windowsize> (The size of the window, default is 25)"
	print """\t-t <type> <num> (type can be sequential, random, or set (default),
			set will have to have a num after it default is 255"""
	if "-f" in sys.argv:
		fileindex = sys.argv.index('-f')
		filename = sys.argv[fileindex + 1]
		if filename[-4:] != '.csv':
			filename += '.csv'
	else:
		filename = 'random_data.csv'
	
	if '-n' in sys.argv:
		numindex = sys.argv.index('n')
		num = int(sys.argv[numindex + 1])
	else:
		num = 10000

	if 'w' in sys.argv:
		windowindex = sys.argv.index('-w')
		window = int(sys.argv[windowindex + 1])
	else:
		window = 25

	setnum = 0
	if '-t' in sys.argv:
		typeindex = sys.argv.index('-t')
		datatype = sys.argv[typeindex + 1]
		print "Here is the datatype {}".format(datatype)
		if datatype == 'set':
			try:
				setnum = int(sys.argv[typeindex + 2])
				print setnum
			except:
				setnum = 255
				pass
		print "Here is the num for set {}".format(setnum)
		if datatype not in ['sequential', 'random', 'set']:
			raise Exception("Not a valid selection, must be sequential, random, or set")
	else:
		datatype = 'set'
		setnum = 255

	randdatagenerator(filename, num, window, datatype, setnum)
