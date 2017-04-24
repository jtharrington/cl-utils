#! /usr/bin/python

import sys
array = []
mean = 0
meansum = 0
distancesum = 0
i = 0
for line in sys.stdin:
	line = line.strip()
	num = float(line)
	array.append(num)
	meansum += num 
	i += 1
mean = meansum / (i-1)

for a in array:
	d = a - mean
	distance = d**2
	distancesum += distance
stddev = (distancesum/(i-1))**0.5
uncertainty = stddev/(mean**0.5)
print uncertainty
