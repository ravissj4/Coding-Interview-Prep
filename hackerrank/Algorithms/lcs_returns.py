#!/bin/python3

import os
import sys

#
# Complete the tutzkiAndLcs function below.
#
def tutzkiAndLcs(a, b):
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = tutzkiAndLcs(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
