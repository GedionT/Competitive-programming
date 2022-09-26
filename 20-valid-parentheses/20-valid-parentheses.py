class Solution:
    def isValid(self, s: str) -> bool:
        """
            
            ( ) [ ] { }
            
        """
        
        match = {
                  '(': ')',
                  '{': '}',
                  '[': ']'
                }
        
                
        # sanity check
        if s[0] not in match.keys():
            return False
    
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and stack[-1] in match and s[i] == match[stack[-1]]:
                stack.pop()
            else:
                stack.append(s[i])
            
        return True if not stack else False
            
            
                
                
            
            
            
        

        