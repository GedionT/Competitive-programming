from ast import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        # O(n^2)
        
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
        
    # O(n) time, using a monotonic stack not solved yet

    def subArrayRanges(self, nums: List[int]) -> int:
            
            # O(n)
            
            n = len(nums)
            total = 0
            stack = []
            
            for i in range(n):
                
                while stack and nums[i] < nums[stack[-1]]:
                    small = nums[stack.pop()]
                    large = nums[i]
                    total += large - small
                
                stack.append(i)
            
            return total