class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def dfs(c):
            if c in memo: return memo[c]
            memo[c] = dfs(c-1) + dfs(c-2)
            return memo[c]
        
        return dfs(n)
            