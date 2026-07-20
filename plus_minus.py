#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    denominator = len(arr)
    p = 0
    n = 0
    z = 0 
    for num in arr:
        if num > 0:
            p += 1
        elif num < 0:
            n += 1
        else:
            z += 1
    if p != 0:
        print(p/denominator)
    else:
        print(0)
    if n != 0:
        print(n/denominator)
    else:
        print(0)
    if z != 0:
        print(z/denominator)
    else:
        print(0)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
