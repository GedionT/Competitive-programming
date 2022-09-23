class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
            4
            
            ans - 0110 
            
            1 - 0100
            
            2 - 10
            
            3 - 11
            
            
        """
        
        s = 0
        for i in range(1, n+1):
            s = ( s << len((bin(i)[2:])) | i ) % (10**9+7)
        return s
    