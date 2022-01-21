#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n, m = map(int, input().strip().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda x: x[k])

    for l in arr:
        print(*l, sep=' ')
