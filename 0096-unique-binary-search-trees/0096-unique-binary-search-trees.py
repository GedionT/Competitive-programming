class Solution:
    def numTrees(self, n: int) -> int:
        
        fact = math.factorial
           
        # usin catalan's number formula
        return fact(2*n) // (fact(n+1) * fact(n))