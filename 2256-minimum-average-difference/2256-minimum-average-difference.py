class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_avg_diff = float('inf')
        res = -1
        
        prefix = [nums[0]]
        suffix = [nums[-1]]
        
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            suffix.append(suffix[-1] + nums[i])
        suffix = suffix[::-1]
                
        for i in range(len(nums)):
            if i+1 == len(nums):
                curr_avg_diff = prefix[i]//(i+1)
            else:
                curr_avg_diff = abs( (prefix[i]//(i+1)) - ((suffix[i] - nums[i]) // (len(nums) - (i+1))) )
            
            if curr_avg_diff < min_avg_diff:
                min_avg_diff = curr_avg_diff
                res = i
            
        return res
        