class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
#       iterative approach in reverse order computation  
#         cost.append(0)
        
        
#         for i in range(len(cost)-3, -1, -1):
#             cost[i] += min(cost[i+1], cost[i+2])
            
        
#         return min(cost[0], cost[1])
    
    
        dp = [0]* (len(cost))
        i = 0
        while i < len(cost):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            i+= 1
            
        return min(dp[-1],dp[-2])