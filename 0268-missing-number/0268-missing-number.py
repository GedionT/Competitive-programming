class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        sequence_summation = n * (n+1) // 2
        wrong_sum = sum(nums)
        
        return sequence_summation - wrong_sum
            