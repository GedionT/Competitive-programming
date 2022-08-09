class Solution:
    def fib(self, n: int, saved = {}) -> int:
        
        if n in saved:
            return saved[n]
        
        if n == 0:
            return 0
        
        if n <= 2:
            return 1
        
        s = self.fib(n-1, saved) + self.fib(n-2, saved)
        saved[n] = s
        return s