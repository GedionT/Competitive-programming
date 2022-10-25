class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # @lru_cache(None)
        # @cache
        memo = {}
        def dp(total):
            if total == amount:
                return 0
            
            if total > amount:
                return float('inf')
            
            if total in memo:
                return memo[total]
            
            ans = float('inf')
            
            for coin in coins:
                ans = min(ans, dp(total+coin)+1)
            
            memo[total] = ans
            return ans
        
        res = dp(0)
        return res if type(res) == int else -1