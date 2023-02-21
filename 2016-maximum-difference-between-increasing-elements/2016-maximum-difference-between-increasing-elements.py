class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        curr_min = nums[0]
        ans = 0
        
        for num in nums:
            if num < curr_min:
                curr_min = num
                
            ans = max(ans, num-curr_min)
            
        return -1 if ans == 0 else ans 