#!/usr/bin/env python
import sys


#TODO

currentWord = None
totalCount = 0
totalWordCount = {}
listSorted = []

for line in sys.stdin:
	key, value = line.split( '\t' )
	if key != currentWord:
		if currentWord is not None:
			totalWordCount[currentWord] = totalCount
		currentWord = key
		totalCount = 0
	totalCount = totalCount + int(value)
totalWordCount[currentWord] = totalCount
word_count_d1 = {k : v for k,v in totalWordCount.iteritems() if v in [0]}
listSorted = sorted(word_count_d1)
for line in listSorted:
	print '%s' % (line)
  # TODO

#TODO
