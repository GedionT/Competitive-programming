
from typing import List
import math
import os
import random
import re
import sys


def insertSort(n, rawArray):
    '''
    The function accepts Integer n param and Integer_Array arr param
    '''
    lastElement = rawArray[len(rawArray)-1]

    for index in range(len(rawArray)-2, 0, -1):
        if rawArray[index] > lastElement:
            rawArray[index+1] = rawArray[index]
            print(rawArray)
        else:
            rawArray[index+1] = lastElement
            print(rawArray)
            continue


if __name__ == "__main__":
    # n = int(input().strip())
    n = 5
    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 4, 5, 3]

    insertSort(n, arr)
