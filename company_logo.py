#!/bin/python3

import math
import os
import random
import re
import sys

def company_logo(s):
    counter = {}
    for i in range(len(s)):
        if s[i] in counter:
            counter[s[i]] += 1
        else:
            counter[s[i]] = 1

    ordered = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    for letter, frequency in ordered[:3]:
        print(letter, frequency)

if __name__ == '__main__':
    s = input()
    company_logo(s)
