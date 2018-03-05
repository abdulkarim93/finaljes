#!/usr/bin/env python

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


with open(stopWordsPath) as f:
	stopWordsList = []
	for l in f:
		stopWordsList.append(l.strip('\n'))

with open(delimitersPath) as f:
	delimiters = []
	while True:
		c=f.read(1)
		if not c:
			break
		delimiters.append(c)

def tsplit(s, sep):
	stack = [s]
	for char in sep:
		pieces = []
		for substr in stack:
			pieces.extend(substr.split(char))
		stack = pieces
	return stack

delimiters.append("\n")
list1 = []
for line in sys.stdin:
	list1.append(line.strip('\n').decode("utf-8-sig").encode('utf8'))

lengthList = len(list1)
list2 = []
i = 0
while i < lengthList:
	temp = list1[i]
	temp1 = temp.lower()
	temp2 = tsplit(temp1,delimiters)
	list2.append(temp2)
	i += 1

list3 = []
for line in list2:
	for y in line:
		list3.append(y)

while '' in list3:
	list3.remove('')

sublist4 = []
for line in list3:
	if line not in stopWordsList:
		sublist4.append(line)

for line in sublist4:
	print '%s\t%s' % (line, "1")
	
  

