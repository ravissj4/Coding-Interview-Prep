#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird_dict = {}
    for i in range(1, 6):
        bird_dict[i] = 0

    for i in range(len(arr)):
        bird_dict[arr[i]] += 1

    highest = 0
    highest_type = -1
    for type in bird_dict:
        if bird_dict[type] > highest:
            highest = bird_dict[type]
            highest_type = type
    return highest_type
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
