class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        L, R = 0, len(tokens)-1
        score, res = 0, 0
        
        while L <= R:
            if tokens[L] <= power:
                power-=tokens[L]
                score+=1
                res = max(score, res)
                L+=1
            elif score >= 1:
                power+=tokens[R]
                score-=1
                R-=1
            else:
                break
        return res