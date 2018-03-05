#!/usr/bin/env python
import sys
#TODO

currentWord = None
totalCount = 0
totalWordCount = {}
listSorted = []
# input comes from STDIN
for line in sys.stdin:
	key, value = line.split( '\t' )
	if key != currentWord:
		if currentWord is not None:
			totalWordCount[currentWord] = totalCount
		currentWord = key
		totalCount = 0
	totalCount = totalCount + int(value)
totalWordCount[currentWord] = totalCount
#list = sorted(totalWordCount, key=lambda key: (-totalWordCount[key], key))
list = sorted(totalWordCount.keys() ,reverse=True)
#print list
values = []
for i in list:
	values.append(totalWordCount[i])
#print values
list1 = sorted(totalWordCount.values())
#print list1
index = [list1.index(v) for v in values]
#print index
i = 0
z = len(list)
while i < z:
	print "%s\t%s" % (list[i],str(index[i]))
	i += 1
	

    # TODO


#TODO
