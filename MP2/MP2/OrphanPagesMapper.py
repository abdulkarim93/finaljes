#!/usr/bin/env python
import sys

def tsplit(s, sep):
	stack = [s]
	for char in sep:
		pieces = []
		for substr in stack:
			pieces.extend(substr.split(char))
		stack = pieces
	return stack
list1 = []
for line in sys.stdin:
	list1.append(line.strip('\n'))

delimiters = [" "]
z = len(list1)
list2 = []
wordCount = 0
while wordCount < z:
	temp = list1[wordCount]
	temp2 = tsplit(temp,delimiters)
	list2.append(temp2)
	wordCount += 1

list3 = []
for line in list2:
	for y in line:
		list3.append(y)

while '' in list3:
	list3.remove('')

for line in list3:
	if ":" in line:
		print '%s\t%s' % (line.rstrip(':'), "0")
	else:
		print '%s\t%s' % (line, "1")
		
  # TODO
