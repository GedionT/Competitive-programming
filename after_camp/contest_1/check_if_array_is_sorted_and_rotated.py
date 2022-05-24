from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        
        min_index = nums.index(min(nums))

        if len(nums) == 1:
            return True
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if i != min_index:
                    return False

        return True