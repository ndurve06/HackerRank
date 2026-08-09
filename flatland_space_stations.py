#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
"""def flatlandSpaceStations(n, c):
    overall_distance = 0
    for i in range(n):
        if i in c:
            continue
        distance = []
        for j in range(len(c)):
            d = abs(i - c[j])
            distance.append(d)
        minimum = min(distance)
        if minimum  > overall_distance:
            overall_distance = minimum
    return overall_distance
    # attempt 1: valid solution, time exceeded
    # """

def flatlandSpaceStations(n, c):
    c.sort()
    overall_distance = 0

    overall_distance = max(overall_distance, c[0] - 0)

    for i in range(1, len(c)):
        gap = (c[i] - c[i-1]) // 2
        overall_distance = max(overall_distance, gap)

    overall_distance = max(overall_distance, (n - 1) - c[-1])
    
    return overall_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
