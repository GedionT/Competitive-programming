class Solution:
    def findComplement(self, num: int) -> int:
        
        ans = ""
        
        # shift the number by 1 each round (sliding the number)
        # do an and with one to look at the last digit and do state change
        while num:
            if num & 1 == 0:
                ans = "1" + ans
            else:
                ans = "0" + ans
            num = num >> 1
        
        return int(ans, 2)