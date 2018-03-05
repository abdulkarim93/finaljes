#!/usr/bin/env python
import sys



#TODO
totalCount = 0
minValue = 99999999999
maxValue = 0
VarianceNO = 0
avg = 0
words_count = []
for line in sys.stdin:
	k, v = line.split( '\t' )
	totalCount = totalCount + int(v)
	if (int(v) < minValue):
		minValue = int(v)
	if (int(v) > maxValue):
		maxValue = int(v)
	words_count.append(int(v))	

avg = totalCount/len(words_count)
for count in words_count:
	VarianceNO = VarianceNO + ((count - avg)**2)
VarianceNO = VarianceNO/len(words_count)

print '%s\t%s' % ("Mean",str(avg))
print '%s\t%s' % ("Sum",str(totalCount))
print '%s\t%s' % ("Min",str(minValue))
print '%s\t%s' % ("Max",str(maxValue))
print '%s\t%s' % ("Var",str(VarianceNO))

    # TODO

#TODO
