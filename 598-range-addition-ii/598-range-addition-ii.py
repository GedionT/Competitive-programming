class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        if not ops:
            return m * n
      
        #finding minimum area of overlap
        min_row = float('inf')
        min_col = float('inf')

        for i in ops:
            min_row = min(min_row, i[0])
            min_col = min(min_col, i[1])

        return min_row * min_col