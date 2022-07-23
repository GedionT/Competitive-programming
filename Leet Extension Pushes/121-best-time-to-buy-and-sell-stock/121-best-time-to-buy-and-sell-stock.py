class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        7, 1, 5, 3, 6, 4
        
        
        dp = [0] * len(prices)
        buy = prices[0]
        
        for i, p in enumerate(prices):
            buy = min(buy, p)
            dp[i] = max(prices[i] - buy, dp[i-1])
            
        return dp[-1]