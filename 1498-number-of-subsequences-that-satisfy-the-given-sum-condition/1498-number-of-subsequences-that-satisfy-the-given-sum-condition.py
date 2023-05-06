class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        mod = 10**9+7
        nums.sort()
        
        res = 0
        
        l = 0
        r = len(nums)-1
        
        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + pow(2, r - l, mod)) % mod
                l += 1
            else:
                r -= 1
                
        return res