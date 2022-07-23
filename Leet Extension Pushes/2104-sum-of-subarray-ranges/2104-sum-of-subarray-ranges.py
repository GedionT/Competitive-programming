class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        total = 0
        
        for i in range(n):
            
            small = nums[i]
            large = nums[i]
            
            for j in range(i+1, n):
                small = min(nums[j], small)
                large = max(nums[j], large)
                
                total += large - small
        
        return total
        