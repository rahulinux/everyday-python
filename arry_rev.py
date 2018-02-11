#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

#while n > 0:
#    n = n - 1
#    print arr[n],

print ' '.join( str(i) for i in arr[::-1] )
