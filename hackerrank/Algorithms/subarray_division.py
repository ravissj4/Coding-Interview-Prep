#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    sum = 0
    for i in range(0, m):
        sum += s[i]
    ans = 0
    if sum == d:
        ans += 1
    
    l = 0
    for r in range(m, len(s)):
        sum = sum + s[r] - s[l]
        l += 1
        if sum == d:
            ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
