#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    arr_frequency = {}
    brr_frequency = {}
    for num in arr:
        arr_frequency[num] = arr_frequency.get(num, 0) + 1
    for num in brr:
        brr_frequency[num] = brr_frequency.get(num, 0) + 1

    missing = []
    for num in brr_frequency:
        if brr_frequency[num] > arr_frequency.get(num, 0):
            missing.append(num)

    missing.sort()
    return missing

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
