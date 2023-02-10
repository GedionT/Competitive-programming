class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        nums = list(map(lambda x: pow(x,2), nums))
        
        return sorted(nums)