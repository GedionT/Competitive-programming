class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        """
        2, 5, 3, 9, 5, 3
        
        2  7  10 19  24 27
        27 25 20  17  8  3
        """
        min_avg_diff = (float('inf'), 0)
        
        forward_prefix = [nums[0]]
        backward_prefix = [nums[-1]]
        
        for i in range(1, len(nums)):
            forward_prefix.append(forward_prefix[-1] + nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            backward_prefix.append(backward_prefix[-1] + nums[i])
        backward_prefix = backward_prefix[::-1]
        
        print(forward_prefix, backward_prefix)
        
        for i in range(len(nums)):
            if i+1 == len(nums):
                curr_avg_diff = forward_prefix[i]//(i+1)
            else:
                curr_avg_diff = abs( (forward_prefix[i]//(i+1)) - ((backward_prefix[i] - nums[i]) // (len(nums) - (i+1))) )
            curr_avg_diff = (curr_avg_diff, i)
            min_avg_diff = min(min_avg_diff, curr_avg_diff)
            
        return min_avg_diff[1]    # this code will fail because won't find the smallest i
                                  # lesson: min can work on tuple by looking at first index
                                  # can override based on d/t key arg on the min function
        
        