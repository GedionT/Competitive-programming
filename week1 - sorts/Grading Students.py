#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List
#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades) -> List[int]:
    # Write your code here

    adjusted_grades = []

    for grade in grades:
        if grade < 38:
            adjusted_grades.append(grade)
        elif grade % 5 < 3:
            adjusted_grades.append(grade)
        elif grade % 5 >= 3:
            adjustment_rate = 5 - (grade % 5)
            adjusted_grades.append(grade + adjustment_rate)
        else:
            continue

    return adjusted_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
