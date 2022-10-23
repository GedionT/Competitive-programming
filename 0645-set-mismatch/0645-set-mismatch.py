class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        big = small = 0
        for num in count:
            if count[num] == 2:
                big = num
                
        hole = [0]*len(nums)
        for c in count:
            hole[c-1] += 1
            
        idx = hole.index(0)+1
        
        return [big , idx]
        