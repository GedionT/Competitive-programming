class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def check(n):
            count = 0
            for i in nums:
                if i <= n:
                    count += 1
            return count <= n    
        
        
        l, r = 1, len(nums)
        ans = 0
        
        while l <= r:
            mid = l + (r - l)//2
            
            if not check(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
            
        return ans