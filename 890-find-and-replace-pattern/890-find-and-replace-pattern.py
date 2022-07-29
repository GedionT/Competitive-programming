class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        # abc, deq, mee, aqq      - abb
        # mee, aqq
        
        # mapping forward and backward with two dicts and checking 
        
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1:m1[w] = p
                if p not in m2: m2[p] = w
                    
                if (m1[w], m2[p]) != (p, w):
                    return False
                
            return True
        
        return filter(match, words)