class Solution:
    def findComplement(self, num: int) -> int:
        
        ans = 0
        shift_count = 0
        
        while num:
            if num & 1 == 0:
                ans = ans | 1 << shift_count
            
            shift_count += 1
            num = num >> 1
        
        return ans