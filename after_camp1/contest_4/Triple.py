from typing import List


def triple(arr: List) -> int:

    arr.sort()

    # count any number appearing more than 3 times
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] == arr[i+2]:
            return arr[i]

    return -1


num_test = int(input())

for _ in range(num_test):
    size = int(input())
    arr = list(map(int, input().split()))

    print(triple(arr))
