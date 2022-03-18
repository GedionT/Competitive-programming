class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(x):
            s = 0
            for n in nums:
                s += math.ceil(n / x)
            return s <= threshold
        
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left