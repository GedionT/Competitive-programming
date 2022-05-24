from typing import List

cols = int(input())


def num_hiding(order: List) -> int:

    count = 0
    order = order[::-1]

    stack = []

    stack.append(order[0])
    for i in range(1, len(order)):
        if order[i] < stack[-1]:
            count += 1
        else:
            stack.append(order[i])

    return count


for _ in range(cols):
    number_per_col = int(input())
    order = list(map(int, input().split()))
    print(num_hiding(order))


# check bruteforce approach with n^2 time complexity