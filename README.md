#Purpose
Generates random data to train the neural network

##Test data types
* set data:
** This will be only one number for the entire csv, and you can specify the set number
* sequential data:
** The first row will always be [255] * the window size, and each row will be decreasing from the one before it. If it gets to [0] * window size before the end of the amount of lines you want, then the rest of the file will be all zeros
* random data:
** all random numbers ranging from 0 to 255
