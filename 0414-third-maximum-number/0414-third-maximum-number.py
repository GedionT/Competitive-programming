class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(set(nums)) < 3:
            return max(nums)
        
        nums = list(set(nums))
        nums.sort()
        return nums[-3]