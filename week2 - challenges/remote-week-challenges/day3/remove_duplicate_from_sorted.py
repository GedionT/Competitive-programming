#  time taken -> 15 minutes

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if(nums[i-1] != nums[i]):
                nums[index] = nums[i]
                index += 1
        return index


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))
