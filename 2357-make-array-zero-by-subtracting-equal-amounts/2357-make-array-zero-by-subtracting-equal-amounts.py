class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        if 0 in nums:
            return len(nums) - 1
        
        return len(nums)
        