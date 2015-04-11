#!/usr/bin/python
# Randomizes a list of words from a plain text file.

import sys
import os
from random import randint

out = []

filename = sys.argv[1]
fileexists = os.path.exists(str(filename))

# if invalid file, exit
if not fileexists:
	sys.exit(str(filename) + ' does not exist')

f = open(filename, 'r')

i = 0
lines = f.readlines()
nlines = len(lines)

for i in range(0, nlines - 1):
	r = randint(0, nlines - i - 1)
	out.append(lines[r])
	lines.remove(lines[r])

for item in out:
	print item,

	
