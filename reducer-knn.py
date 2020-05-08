#!/usr/bin/python3

from itertools import groupby
from operator import itemgetter
import sys
k = 11
group_comparator = lambda x: x[:-1]
arr = []
for l in sys.stdin:
	l=l.strip()
	dists,data = l.split(',',1)
	arr.append(data.split(','))

for key, group in groupby(arr,group_comparator):
	count = 0
	temp_c = []
	for row in group:
		temp_c.append((row[-1]))
		count += 1
		if count >= k: break
	label = max(temp_c,key=temp_c.count)
	print(','.join(key), ',', label)