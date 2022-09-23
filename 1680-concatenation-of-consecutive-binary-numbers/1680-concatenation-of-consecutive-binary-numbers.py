class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ''
        for i in range(n+1):
            s += str(bin(i)[2:])
        
        dec = int(s, 2) % (10**9 + 7)
        
        return dec