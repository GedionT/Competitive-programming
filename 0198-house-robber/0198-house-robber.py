class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
            1 2 3 1
            
            1 2 4 4
            
            init two vars with val of 0 and max 0, 1 idx elments
        """
        
        if len(nums) <= 2:
            return max(nums)
        
        first = nums[0]
        second = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            first, second = second, max(first + nums[i], second)
        
        return second