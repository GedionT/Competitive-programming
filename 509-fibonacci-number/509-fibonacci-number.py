class Solution:
    def fib(self, n: int) -> int:
        
        last2, last = 0, 1
        
        for i in range(n):
            last2, last = last, last2 + last
        
        return last2
        
        