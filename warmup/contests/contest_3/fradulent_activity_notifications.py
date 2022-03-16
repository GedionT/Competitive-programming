#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

###################################################################################################
###################################################################################################
###################################################################################################

def activityNotifications(expenditure, d) -> int:
    # Write your code here
    notification = 0
    count = [0]*202

    # creating a count array to store the number of times a number appears
    for day in range(d):
        count[expenditure[day]] += 1

    old = 0
    for i in range(d, len(expenditure)):
        limit = get_limit(count, d)
        # print(limit)

        if expenditure[i] >= limit:
            notification += 1

        count[expenditure[old]] -= 1
        count[expenditure[i]] += 1
        old += 1

    return notification


# function accepts the count array of size 202 and d, the number of trailing days to be considered
# returns the limit for the trailing days

def get_limit(count, d) -> int:

    temp, left, right = 0, -1, -1

    # check oddity of the number of times a number appears
    # the median calculation will be based on this
    if d % 2 != 0:
        for i, v in enumerate(count):
            temp += v

            if temp > ((d//2)):
                return i*2

    # calculate the median and return the maximum limit allowed
    else:
        for i, v in enumerate(count):
            temp += v

            if temp == (d//2):
                left = i
                right = i+1

                return ((left+right) / 2)*2

            if temp > (d//2):
                return i*2

###################################################################################################
###################################################################################################
###################################################################################################


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
