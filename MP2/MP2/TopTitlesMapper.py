#!/usr/bin/env python
import sys




currentWordCount = {}
list1 = []
for l in sys.stdin:
	key, value = l.split( '\t' )
	currentWordCount[key] = int(value)
	list1.append(key)

sortlist = sorted(list1[0:10])
for l in sortlist[0:10]:
	print '%s\t%s' % (l,str(currentWordCount[l]) )



