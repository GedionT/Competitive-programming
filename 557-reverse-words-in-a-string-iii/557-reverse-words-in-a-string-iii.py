class Solution:
    def reverseWords(self, s: str) -> str:
        new = ""
        for w in s.split(" "):   
            new += w[::-1] + " "
        return new[:-1]
        
        
            
        