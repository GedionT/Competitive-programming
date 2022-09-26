class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:   
        n = len(cost)
        dp = [0]*n
        
        
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[-1], dp[-2])
            
            
            
          