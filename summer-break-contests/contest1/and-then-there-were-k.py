

"""
Given an integer n, find the maximum value of integer k such that the following condition holds:

n & (n-1) & (n-2) & (n-3) & ... (k) = 0
    where & denotes the bitwise AND operation.

    return the required integer k
"""

# test case 2 not passing
# def find_k(n):

#     # handle edge cases
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     k = n

#     while n:
#         n &= n-1
#         k -= 1

#     return k


# passing solution

import math


def find_k(n):

    sol = (2**int(math.log(n, 2))) - 1
    return sol


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())
        print(find_k(n))


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())
        print(find_k(n))
