#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def checkKaprekar(n, d):
    square = n * n
    str_square = str(square)

    left = str_square[:-d]
    right = str_square[-d:]

    left_num = int(left) if left else 0
    right_num = int(right)

    if left_num + right_num == n:
        return True
    else:
        return False

def kaprekarNumbers(p, q):
    output = ""
    for i in range(p, q + 1):
        if checkKaprekar(i, len(str(i))):
            output += f"{i} "
    if output == "":
        print("INVALID RANGE")
    else:
        print(output)


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
