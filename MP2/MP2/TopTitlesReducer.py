#!/usr/bin/env python
import sys



# input comes from STDIN
for l in sys.stdin:
	key, value = l.split( '\t' )
	wordValue = int(value)
	print '%s\t%s' % (key, str(wordValue))
