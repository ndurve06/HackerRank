#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.lower()
    counter = 0
    alphabet = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    for i in range(len(s)):
        letter = s[i]
        if letter == " ":
            continue
        if alphabet[letter] == 0:
            alphabet[letter] = 1
            counter += 1
            if counter == 26:
                return "pangram"

    return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
