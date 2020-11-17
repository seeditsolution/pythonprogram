#!/bin/python3

import math
import os
import random
import re
import sys
def hourglass(arr):
    l=[]
    summation=0
    for i in range(4):
        for j in range(4):
            summation=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            l.append(summation)
    return max(l)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglass(arr))
