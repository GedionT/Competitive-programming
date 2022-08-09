class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        """
            [2, 7, 9, 3, 1]
            
            dp[0] = 2
            dp[1] = max(2, 7) = 7
            dp[2] = max(7, 2+9 (11)) = 11
            dp[3] = max(11, 7+3 (10)) = 11
            dp[4] = max(11, 11+1 (12)) = 12
            
            
            dp[-1] = max sum 
        
        """
     
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[-1]
        
        
        