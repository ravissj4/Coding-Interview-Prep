#!/bin/python3

import os
import sys

#
# Complete the tutzkiAndLcs function below.
#

def func(c):
    # print(f"c = {c}")
    if c >= 'a' and c <= 'z':
        # print("here 1")
        return ord(c) - ord('a')
    if c >= 'A' and c <= 'Z':
        # print("here 2")
        return ord(c) - ord('A') + 26
    # print("here 3")
    return ord(c) - ord('0') + 52 

def tutzkiAndLcs(a, b):
    N = len(a)
    M = len(b)

    # its like a dictionary key represents a char in int form
    # but not ascii, they are numbered : a-z as 0-25 and A-Z as 
    # 26-51 and 0-9 as 52-61
    # each key/char has a list denoting the positions where it is 
    # present in the string b (would need this later on).
    pos_dict = {}
    for i in range(M):
        # print(f"i = {i}")
        # print(f"func(b[i]) = {func(b[i])}")
        if func(b[i]) in pos_dict:
            pos_dict[func(b[i])].append(i + 1)
        else:
            pos_dict[func(b[i])] = [i+1] 

    # calculating the lcs of every prefix strings from left to right
    rows, cols = (5000, 5000) 
    dpl = [[0 for i in range(cols)] for j in range(rows)] 

    for i in range(1, N+1):
        for j in range(1, M+1):
            if a[i-1] == b[j-1]:
                dpl[i][j] = dpl[i-1][j-1] + 1
            else:
                dpl[i][j] = max(dpl[i-1][j], dpl[i][j-1])
            
    lcs = dpl[N][M]

    # calculating the lcs of every prefix strings from right to left
    dpr = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(N, 0, -1):
        for j in range(M, 0, -1):
            if a[i-1] == b[j-1]:
                dpr[i][j] = dpr[i+1][j+1] + 1
            else:
                dpr[i][j] = max(dpr[i+1][j], dpr[i][j+1])

    # print("Pos dict : ")
    # for key, item in pos_dict.items():
    #     print(f"key = {key} and item = {item}")
    
    # for a particular position i,
    # trying to insert all characters possible from 1 to 62 
    # if they are present in string b. 
    # if present, then we see if the sum of the lcs of string 
    # from a0...ai and b0...x-1 and string ai+1...an and bx+1...bm
    # is equal to the original lcs or not.
    # if its equal, then the insertion of string pos_dict[j] will 
    # result in an increase in the lcs, otherwise not and hence we will check
    # with the next position of string pos_dict[j] in b            
    ans = 0
    for i in range(N+1):
        for j in range(62):
            if j in pos_dict:
                for x in pos_dict[j]:
                    if dpl[i][x-1] + dpr[i+1][x+1] == lcs:
                        ans += 1
                        break
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = tutzkiAndLcs(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
