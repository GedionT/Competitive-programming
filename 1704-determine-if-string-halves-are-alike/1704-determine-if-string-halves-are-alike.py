class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        s = s.lower()
        vowels = [ 'a', 'e', 'i', 'o', 'u']
        
        left = 0
        right = len(s)-1
        
        lc = rc = 0
        
        while left < right:
            
            if s[left] in vowels:
                lc += 1
            
            if s[right] in vowels:
                rc += 1
                
            left += 1
            right -= 1
            
        
        return lc == rc