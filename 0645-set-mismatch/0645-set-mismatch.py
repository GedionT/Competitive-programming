class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        hole = [0]*len(nums)
        for num in nums:
            hole[num-1] += 1
        
        repeat = hole.index(2)+1
        missing = hole.index(0)+1
        
        return [repeat , missing]
        