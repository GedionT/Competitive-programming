from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        
        odd_top = [ (i[1], i[0]) for i in Counter(nums[1::2]).most_common(2) ]
        even_top = [ (i[1], i[0]) for i in Counter(nums[0::2]).most_common(2) ]
        
        
        # if not repeated element, then just choose the high frequency
        if odd_top[0][1] != even_top[0][1]: return len(nums) - odd_top[0][0] - even_top[0][0]
        
        # if have same values in both, then we have 2 scenarios to choose either.
        sit1 = len(nums) - odd_top[0][0] - (even_top[1][0] if len(even_top) > 1 else 0)
        sit2 = len(nums) - even_top[0][0] - (odd_top[1][0] if len(odd_top) > 1 else 0)
        
        return min(sit1, sit2)