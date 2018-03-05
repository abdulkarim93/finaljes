#!/usr/bin/env python
import sys


for l in sys.stdin:
	key,value  = l.split("\t")
	currentWord = int(value)
	print '%s\t%s' % ("Value", str(currentWord))
    # TODO
