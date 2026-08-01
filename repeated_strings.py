#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    full = n // len(s)
    rem = n % len(s)
    a = 0
    
    for i in range(len(s)):
        if s[i] == "a":
            a += 1
    
    a = a * full
    
    for i in range(rem):
        if s[i] == "a":
            a += 1
    
    return a
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
