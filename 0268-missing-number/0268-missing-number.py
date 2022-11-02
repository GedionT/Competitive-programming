class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor1 = len(nums)
        xor2 = nums[0]
        
        for i in range(1, len(nums)):
            xor1 ^= i
            xor2 ^= nums[i]
        
        return xor1 ^ xor2 
            