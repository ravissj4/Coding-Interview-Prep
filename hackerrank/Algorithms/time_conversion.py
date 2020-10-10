#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour_12 = int(s[0:2])
    ampm_12 = s[8:]
    if ampm_12 == 'AM':
        if hour_12 == 12:
            s = '00' + s[2:]
    if ampm_12 == 'PM':
        if hour_12 != 12:
            s = str(hour_12 + 12) + s[2:]
    return s[0:8]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
