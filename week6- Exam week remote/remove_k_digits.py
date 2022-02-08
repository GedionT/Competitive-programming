class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        for i in num:
            while( stack and int(stack[-1]) > int(i) and k):
                stack.pop()
                k -= 1
                
            stack.append(str(i))
        
        # If no elements removed pop elements increasingly
        while(k):
            stack.pop()
            k -= 1

        # handle edge case for zeros in the beginning
        l = 0
        while( l <len(stack) and stack[l] == "0" ):
            l += 1
            
        return ''.join(stack[l:]) if (len(stack[l:]) > 0) else "0"
        