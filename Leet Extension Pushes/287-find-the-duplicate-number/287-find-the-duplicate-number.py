class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        big_one = [0] * 100001
        
        for i in nums:
            if big_one[i] == 0:
                big_one[i] = 1
            else:
                return i