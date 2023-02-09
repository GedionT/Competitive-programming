class Solution:
    def maximumSwap(self, num: int) -> int:
        
        nums = list(str(num))
        
        first = float('-inf')
        second = float('-inf')
        max_idx = len(nums)-1
        
        for i in range(max_idx-1, -1, -1):
            if nums[i] > nums[max_idx]:
                max_idx = i
            
            elif nums[i] < nums[max_idx]:
                first, second = i, max_idx

        if first > -1:
            nums[first], nums[second] = nums[second], nums[first]
            
        return int(''.join(nums))