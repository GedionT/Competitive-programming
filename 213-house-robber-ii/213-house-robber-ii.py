class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        def robber(num):
            first = num[0]
            second = max(num[0], num[1])
            
            
            for i in range(2, len(num)):
                first, second = second, max(second, first + num[i])

            return second
        
        return max(robber(nums[1:]), robber(nums[:-1]))