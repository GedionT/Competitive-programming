class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        mid = pow(2, n-1)

        if n == 1:
            return 0
        elif k > pow(2, n-1)//2:
            return self.kthGrammar(n-1, k - mid)
        else:
            return self.kthGrammar(n-1, k)
