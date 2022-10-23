class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # if sum(nums) < target: # alt edge case handler
        #     return 0
        
        prefix = [0]
        
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        l, r = 0, 1   
        min_window = float('inf')
        
        while r < len(prefix):            
            if prefix[r]-prefix[l] >= target:
                min_window = min(min_window, (r-l))
                l += 1
            else:
                r += 1

        return min_window if type(min_window) == int else 0