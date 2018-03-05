#!/usr/bin/env python
from operator import itemgetter
import sys

currentWord = None
totalWordCount = 0
wordCountTotalCount = {}
# input comes from STDIN
for line in sys.stdin:
	key, value = line.split( '\t' )
	if key != currentWord:
		if currentWord is not None:
			wordCountTotalCount[currentWord] = totalWordCount
		currentWord = key
		totalWordCount = 0
	totalWordCount = totalWordCount + int(value)
wordCountTotalCount[currentWord] = totalWordCount
list = sorted(wordCountTotalCount, key=lambda key: (-wordCountTotalCount[key], key))
for line in list[0:10]:
	print '%s\t%s' % (line, str(wordCountTotalCount[line]))

