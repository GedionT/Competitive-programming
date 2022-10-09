class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = sum(nums[:3])
        

        for i in range(len(nums)-2):
            # update: ignore the duplicate numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums)-1
            
            while l < r:
                _sum = nums[i]+nums[l]+nums[r]
                
                if abs(_sum-target) < abs(res-target):
                    res = _sum
                if _sum < target:
                    l += 1
                elif _sum > target:
                    r -= 1
                else: 
                    return res
        
        return res
        
        
        