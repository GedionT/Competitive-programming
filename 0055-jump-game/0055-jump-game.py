class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for idx in range(len(nums)-2, -1, -1):
            if idx + nums[idx] >= goal:
                goal = idx
            
        return True if goal == 0 else False