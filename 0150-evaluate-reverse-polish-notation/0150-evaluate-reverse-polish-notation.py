class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for tk in tokens:
            
            if tk not in ["+", "-", "*", "/"]:
                stack.append(int(tk))
                
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                
                if tk == "+":
                    stack.append(op2 + op1)
                elif tk == "-":
                    stack.append(op2 - op1)
                elif tk == "*":
                    stack.append(op2 * op1)
                else:
                    q = op2 / op1
                    if q < 0:
                        stack.append(math.ceil(q))
                    else:
                        stack.append(math.floor(q))
        
        return stack[0]
                    
        
