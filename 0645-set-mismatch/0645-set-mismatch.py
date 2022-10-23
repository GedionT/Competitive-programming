class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        big = small = 0

        hole = [0]*len(nums)
        for num in nums:
            hole[num-1] += 1
        
        idx1 = hole.index(2)+1
        idx2 = hole.index(0)+1
        
        return [idx1 , idx2]
        