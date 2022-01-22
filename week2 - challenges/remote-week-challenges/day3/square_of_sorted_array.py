# time taken -> 4 minutes
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i] *= nums[i]

        return sorted(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
