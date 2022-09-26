class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        
        while right < len(prices):
            
            currentProfit = prices[right] - prices[left] #our current Profit
            
            if prices[left] < prices[right]:
                max_profit =max(currentProfit, max_profit)
            else:
                left = right
                
            right += 1
            
        return max_profit
        
        
        
#         # TLE using brute force approach with O(n!) time and o(1) space
#         # [7, 1, 5, 3, 6, 4]
#         #              ^  ^
            
#         max_profit = float("-inf")
        
#         for i in range(len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 max_profit = max((prices[j]-prices[i]), max_profit)
        
#         return 0 if max_profit < 0 else max_profit
    
    
  
        
        