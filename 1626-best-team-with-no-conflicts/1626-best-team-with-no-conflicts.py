class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageAndScore = list(zip(ages, scores))
        
        ageAndScore.sort(key = lambda x: (x[0], x[1]))
        
        dp = [0] * len(scores)
        
        ans = 0
        for i, (_, scr) in enumerate(ageAndScore):
            dp[i] = scr
            for j in range(i):
                if ageAndScore[j][1] <= scr and dp[j] + scr > dp[i]:
                    dp[i] = dp[j] + scr
                    
            if dp[i] > ans:
                ans = dp[i]
                
        return ans