#!/usr/bin/python
import fileinput

#this mapper's really easy: all you have to do is split by ';' and replace '\n' with ''
for line in fileinput.input():				#iteration for each line
	values = line.split(';')				#splitting
	print('{0}\t{1}'.format(values[2],values[6].replace('\n','')))  #print + replace