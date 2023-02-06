class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1
        
        words = sorted(words, key=lambda x: len(x))
        
        chain_dp = {}
        for word in words:
            chain_dp[word] = 1
            
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in chain_dp:
                    chain_dp[word] = max(chain_dp[word], chain_dp[prev]+1)
                    
        return max(chain_dp.values())
        
        