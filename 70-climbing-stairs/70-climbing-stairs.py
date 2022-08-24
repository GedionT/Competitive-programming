class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 : return 1
        if n== 2 : return 2
        first , second = 1, 2
        for i in range(2, n): 
            temp = first + second
            first = second
            second = temp
            
        return second