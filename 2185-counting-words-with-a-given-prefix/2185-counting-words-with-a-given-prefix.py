class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0
        ln = len(pref)
        for word in words:
            if pref == word[0:ln]:
                count += 1
                
        return count