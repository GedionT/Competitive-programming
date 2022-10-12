class Solution:
    def climbStairs(self, n: int) -> int:
        # handle the edge case
        if n == 1: return 1
        if n == 2: return 2

        first, second = 1, 2

        # building the steps iteratively
        for i in range(2, n):
            curr_sum = first + second
            first = second
            second = curr_sum

        # second holds all the moves that I can make using 1, 2 move
        return second


