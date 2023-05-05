class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        left = 0
        right = 0
        count = 0
        maxCount = 0
        
        while right < len(s):
            
            if right - left < k:
                if s[right] in vowels:
                    count += 1
                    maxCount = max(maxCount, count)
                right += 1
            
            else:
                if s[left] in vowels:
                    count -= 1
                left += 1
                
        return maxCount
                
        
        