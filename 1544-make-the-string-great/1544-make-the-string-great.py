class Solution:
    def makeGood(self, s: str) -> str:
        
        goodString = []
        
        
        for c in s:  
            if goodString and abs(ord(goodString[-1]) - ord(c)) == 32:
                goodString.pop()
                continue
            goodString.append(c)
        
        
        return ''.join(goodString)