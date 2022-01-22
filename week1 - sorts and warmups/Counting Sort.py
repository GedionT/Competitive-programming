import random
import re
from typing import List


# Complete the 'countingSort' function

# The function is expected to return an INTEGER_ARRAY
# The function accepts InT Array as param

def countingSort(arr) -> List[int]:

    count_arr = [0, 0, 0, 0, 0]

    for i in range(len(arr)):
        count_arr[arr[i]] += 1

    return count_arr


if __name__ == '__main__':
    n = 5
    arr = [1, 1, 3, 2, 1]

    print(countingSort(n, arr))
