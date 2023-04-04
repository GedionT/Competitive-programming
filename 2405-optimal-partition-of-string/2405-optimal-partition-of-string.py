class Solution:
    def partitionString(self, s: str) -> int:
        
        seen = set()
        count = 0
        
        i = 0
        
        while i < len(s):
            if s[i] not in seen:
                seen.add(s[i])
                
            else:
                seen.clear()
                count += 1
                seen.add(s[i])
                
            i += 1
                
        if seen:
            count += 1
            
        return count