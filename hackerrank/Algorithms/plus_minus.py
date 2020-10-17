#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus_cnt = 0
    minus_cnt = 0
    zero_cnt = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            plus_cnt += 1
        elif arr[i] == 0:
            zero_cnt += 1
        elif arr[i] < 0:
            minus_cnt += 1
        
    print(plus_cnt/n)
    print(minus_cnt/n)
    print(zero_cnt/n)
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
