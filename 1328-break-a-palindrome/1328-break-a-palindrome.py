class Solution:
    def breakPalindrome(self, p: str) -> str:
        
        
        n = len(p)
        if n < 2: return ''
        
        for i in range(n//2):
            
            if p[i] != 'a':
                p = p[:i] + 'a' + p[i+1:]
                break
                
        else: p = p[:-1] + 'b'
            
        return p
            