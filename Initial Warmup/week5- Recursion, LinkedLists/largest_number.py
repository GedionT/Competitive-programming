# from previous weeks

# using greedy approach
# compare from the bottom to the end, the last one is the biggest

from typing import List


class Solution:
    def largestNumber(self, num: List[int]) -> str:

        # change each element to string
        # sort with descending order with ascii order

        num_str = list(map(str, num))

        for i in range(len(num_str)-1, 0, -1):
            for j in range(len(num_str) - 1):
                if num_str[j] + num_str[j+1] < num_str[j+1] + num_str[j]:
                    num_str[j], num_str[j+1] = num_str[j+1], num_str[j]

        return str(int(''.join(num_str)))
