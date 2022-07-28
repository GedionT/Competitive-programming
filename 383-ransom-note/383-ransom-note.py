class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        magAlpha = defaultdict(int)
        
        for char in magazine:
            magAlpha[char] += 1
            
        for char in ransomNote:
            if magAlpha[char] >= 1:
                magAlpha[char] -= 1
            else:
                return False
        
        return True