class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        l, r = 0, len(palindrome)-1
        pal = list(palindrome)
        
        while l < r:
            if pal[l] != "a":
                pal[l] = "a"
                return "".join(pal)
            
            l += 1
            r -= 1
            
        # if it's an all 'a' 
        pal[-1] = "b"
        
        return "".join(pal)
            