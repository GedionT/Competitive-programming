class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        s = list(s.lower())
        
        data = []
        for char in s:
            if char.isalnum():
                data.append(char)
        
        left, right = 0,  len(data)-1
        while left < right:
            if data[left] == data[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
                
        