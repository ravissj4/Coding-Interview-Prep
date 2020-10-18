#!/bin/python3

import math
import os
import random
import re
import sys

def IsLeapYear(year, category):
    if category == 1:
        if year % 4 == 0: 
            return True
    if category == 2 or category == 3:
        if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
            return True
    return False
def findCategory(year):
    if year >= 1700 and year <= 1917:
        return 1
    elif year == 1918:
        return 2
    else:
        return 3

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    category = findCategory(year)
    if category == 1:
        if IsLeapYear(year, category):
            return f"12.09.{year}"
        else :  
            return f"13.09.{year}"
    elif category == 2:
        if IsLeapYear(year, category):
            return f"12.10.{year}"
        else:    
            return f"13.10.{year}"
    elif category == 3:
        if IsLeapYear(year, category):
            return f"12.09.{year}"
        else:    
            return f"13.09.{year}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
