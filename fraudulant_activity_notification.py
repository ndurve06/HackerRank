#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

# First attempt, correct but time exceeded
"""def activityNotifications(expenditure, d):
    notice = 0
    for i in range(d, len(expenditure)):
        sub_list = expenditure[i - d : i]
        sub_list.sort()
        if d % 2 == 0:
            left = sub_list[d//2 -1]
            right = sub_list[d//2]
            median = (left + right) / 2
        else:
            index = d // 2
            median = sub_list[index]
        if expenditure[i] >= median * 2:
            notice += 1
    return notice"""

def calculate_median(frequency, d):
        count = 0
        if d % 2 == 1:
            mid = d//2 + 1 
            for i in range(201):
                count += frequency[i]
                if count >= mid:
                    return i
        else:
            mid1 = d// 2
            mid2 = mid1 + 1
            m1 = None
            m2 = None
            for i in range(201):
                count += frequency[i]
                if m1 is None and count >= mid1:
                    m1 = i 
                if count >= mid2:
                    m2 = i
                    break
        return (m1 + m2) / 2

def activityNotifications(expenditure, d):
    frequency = [0] * 201
    notice = 0 

    for i in range(d):
        frequency[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        median = calculate_median(frequency, d)
        if expenditure[i] >= median * 2:
            notice += 1
        frequency[expenditure[i -d]] -= 1
        frequency[expenditure[i]] += 1

    return notice    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
