class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        running_sum = [nums[0]]
        
        
        for i in range(1, len(nums)):
            running_sum.append(running_sum[-1] + nums[i])
        
        return running_sum