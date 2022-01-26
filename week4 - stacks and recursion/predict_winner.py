from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        # because the selection of the greatest ending is not always
        # good cause you might be leaving or giving leeway to a bigger fish
        # a game theory where lookup and selections are tied

        # can look up manually, but don't know depth

        # if nums.length is even, player 1 has all the odds to win by forcing to choose
        # all the odds or all the evens by computing max sum
        # that means if even length player 1 will always win
        n = len(nums)

        if n % 2 == 0:
            return True

        # else we need a dp to compute max sum of selected/unselected
        # make use of cumulative sum table for speed sum and concise
    """        
            [1, 4, 5, 8, 6, 6]
            
            a - 6   [1, 4, 5, 8, 6, x]
            b - 6   [1, 4, 5, 8, x, x]
            a - 8   [1, 4, 5, x, x, x]
            b - 5   [1, 4, x, x, x, x]
            a - 4   [1, x, x, x, x, x]
            b - 1   [x, x, x, x, x, x]
    

            # 6+8+4=18  >  6+5+1=12 - T
    """
    # a dp solution to compute max sum of selected/unselected
    # use a cumulative sum to compute best choice
    dp = [[0] * n for _ in range(nums)]
    for i in range(nums):
        for j in range(i+1, nums):
            # if we choose i, j, then we can choose i+1, j-1, i+2, j-2, ..., n-1
            # if we choose j, i, then we can choose j+1, i-1, j+2, i-2, ..., n-1
            # so we can choose i, j, i+1, j-1, i+2, j-2, ..., n-1
            # so we can choose j, i, j+1, i-1, j+2, i-2, ..., n-1
            # so we can choose i, j, i+1, j-1, i+2, j-2, ..., n-1
            # so we can choose j, i, j+1, i-1, j+2, i-2, ..., n-1
            # so we can choose i, j, i+1, j-1, i+2, j-2, ..., n-1
            # so we can choose j, i, j+1, i-1, j+2, i-2, ..., n-1
            # so we can choose i, j, i+1, j-1, i+2, j-2, ..., n-1
            # so we can choose j, i, j+1, i-1, j+2, i-2, ..., n-1
            # so we can choose i, j, i+1, j-1, i+2, j-2, ..., n-1
            # so we can choose j, i, j+1, i-1, j+2, i-2, ..., n-1
            # so we can choose i, j, i+1, j-1, i+2, j-2, ..., n-1
            # so we can choose j, i, j+1, i-1, j+2, i-2, ..., n-1
            # so we can choose i, j, i+1, j-1, i+2, j-2,

            dp[i][j] = max(nums[i] + dp[i+1][j], nums[j] + dp[i+1][j+1])
