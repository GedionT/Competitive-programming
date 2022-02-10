class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        left, preSum  = 0, 0
        
        nums.sort()
        
        for i in range(len(nums)):
            
            preSum += nums[i]
            if preSum + k < nums[i] * (i - left + 1):
                preSum -= nums[left]
                left += 1
            
        return len(nums) - left
    