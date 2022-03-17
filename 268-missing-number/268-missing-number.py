class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        big = [0] * 10001
        for i in nums:
            big[i] = 1
        
        for j in range(len(nums) + 1):
            if big[j] == 0:
                return j