class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        original, reved = x, 0
        
        while x > 0:
            reved = (reved * 10) + x%10 
            x //= 10
            
        return original == reved
 

        
#         s = str(x)
        
#         left = 0
#         right = len(s)-1
        
#         while left <= right:
            
#             if s[left] == s[right]:
#                 left += 1
#                 right -= 1
            
#             else:
#                 return False
        
#         return True