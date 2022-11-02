class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        ans = 0
        shift_count = 0
        
        while n:
            if n & 1 == 0:
                ans = ans | 1 << shift_count
            
            shift_count += 1
            n = n >> 1
        
        return ans