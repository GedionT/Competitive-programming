#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#


def bonAppetit(bill, k, b):
    # Write your code here

    _sum = sum(bill)

    bill.pop(k)
    sum_with_out_anna = sum(bill)

    if b == sum_with_out_anna/2:
        print("Bon Appetit")
    else:
        print(f'{int((_sum/2)-(sum_with_out_anna/2))}')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
