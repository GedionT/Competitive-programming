class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_avg_diff = float('inf')
        mins = []
        
        forward_prefix = [nums[0]]
        backward_prefix = [nums[-1]]
        
        for i in range(1, len(nums)):
            forward_prefix.append(forward_prefix[-1] + nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            backward_prefix.append(backward_prefix[-1] + nums[i])
        backward_prefix = backward_prefix[::-1]
                
        for i in range(len(nums)):
            if i+1 == len(nums):
                curr_avg_diff = forward_prefix[i]//(i+1)
            else:
                curr_avg_diff = abs( (forward_prefix[i]//(i+1)) - ((backward_prefix[i] - nums[i]) // (len(nums) - (i+1))) )
            min_avg_diff = min(min_avg_diff, curr_avg_diff)
            mins.append((min_avg_diff, i))
        
        mins.sort()
            
        return mins[0][1]
        