class Solution:
    def maximum69Number (self, num: int) -> int:
        
        n = list(str(num))
        
        for idx in range(len(n)):
            if n[idx] == '6':
                n[idx] = '9'
                break
        
        return int(''.join(n))