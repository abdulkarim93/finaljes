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
list = sorted(totalWordCount, key=lambda key: (-totalWordCount[key], key))
for line in list:
	print '%s\t%s' % (line, str(totalWordCount[line]))
    # TODO

# TODO
