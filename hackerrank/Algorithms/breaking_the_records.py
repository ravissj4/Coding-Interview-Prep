#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest = float("-inf")
    lowest = float("inf")
    high_record = low_record = -1
    for score in scores:
        if score > highest:
            highest = score
            high_record += 1
        if score < lowest:
            lowest = score
            low_record += 1
    return [high_record, low_record]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
