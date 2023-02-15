class Solution:
    def checkValidString(self, s: str) -> bool:
        
        small = large = 0
        
        for ch in s:
            small += 1 if ch == '(' else -1
            large += 1 if ch != ")" else -1
            
            if large < 0:
                break
                
            small = max(small, 0)
            
        
        return small == 0