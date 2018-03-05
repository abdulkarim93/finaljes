#!/usr/bin/env python
import sys


# TODO


wordCountTotalCount = {}
list1 = []
for line in sys.stdin:
	key, value = line.split( '\t' )
	wordCountTotalCount[key] = int(value)
	list1.append(key)

sortlist = sorted(list1[0:10])
for line in sortlist[0:10]:
	print '%s\t%s' % (line,str(wordCountTotalCount[line]) )

       #TODO


#TODO
