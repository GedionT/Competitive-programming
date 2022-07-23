# time taken = 7 minutes

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort the list
        # sliding window of size 2 with min function
        # sum up

        nums.sort()

        max_of_min_sum = 0

        for i in range(0, len(nums)-1, 2):  # O(n-1/2)
            max_of_min_sum += min(nums[i], nums[i+1])

        return max_of_min_sum


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 4, 3, 2]
    print(sol.arrayPairSum(nums))
