class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:            
        min_window = float('inf')
        left = 0   
        cumulate = 0
        
        for i in range(len(nums)):
            cumulate += nums[i]
            
            while cumulate >= target:
                min_window = min(min_window, ((i+1) - left))
                cumulate -= nums[left]
                left += 1
                
        return min_window if min_window != float('inf') else 0