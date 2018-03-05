#!/usr/bin/env python
import sys


leaguePath = sys.argv[1]
#TODO


with open(leaguePath) as f:
	leaugeList = []
	for line in f:
		leaugeList.append(line.strip('\n'))
	#TODO



list1 = []
word_count_d = {}
for line in sys.stdin:
	list1.append(line.strip('\n'))
	key, value = line.split( '\t' )
	word_count_d[key] = int(value)
	list1.append(key)

list2 = []
for line in list1:
	if line in leaugeList:
		list2.append(line)

for line in list2:	
	print '%s\t%s' % (line,str(word_count_d[line]) )

       #TODO
