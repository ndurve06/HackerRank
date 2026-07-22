#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    arr.sort()
    counter = {}
    freq = 0
    value = 0
    for num in arr:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    
    for i, j in counter.items():
        if j > freq:
            freq = j
            value = i

    return value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
