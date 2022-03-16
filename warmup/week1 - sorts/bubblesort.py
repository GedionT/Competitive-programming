#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    swaps = 0
    # Write your code here
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swaps += 1

    firstElement = a[0]
    lastElement = a[len(a)-1]

    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {firstElement}')
    print(f'Last Element: {lastElement}')


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
