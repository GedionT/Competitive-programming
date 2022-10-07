class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len1 = len(s1)
        mps1 = collections.Counter(s1)
        
        for i in range(len(s2) - len1+1):
            sub = s2[i:i+len1]
            if mps1 == collections.Counter(sub):
                return True
        return False