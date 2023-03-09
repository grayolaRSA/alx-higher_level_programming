#!/usr/bin/python3

import sys
args = [int(arg) for arg in sys.argv[1:]]
total = sum(args)
print(total)
