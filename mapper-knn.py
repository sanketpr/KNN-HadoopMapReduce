#!/usr/bin/python3

import sys
import re
from math import sqrt

test = (sys.argv[1]).split(',')
test = test[:48]

first_line = True
for line in sys.stdin:
	if first_line: first_line = False;continue 
	line=line.strip()
	row=line.split(',')
	train,label = row[:-1],row[-1]
	dist = sum([(float(test[i])-float(ftr))**2 for i,ftr in enumerate(train)])
	sample = test+[label]
	print(sqrt(dist), ",", ','.join(sample))