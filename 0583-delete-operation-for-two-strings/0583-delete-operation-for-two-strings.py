class Solution:
    def minDistance(self, str1: str, str2: str) -> int:
        
        n = len(str1)
        m = len(str2)

        dp = [[0 for _ in range(m + 1)] for i in range(n + 1) ]

        for i in range(1,  n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        ans = n  + m - 2 * dp[n][m]
        return ans
