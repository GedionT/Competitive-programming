class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        for row in grid:
            for element in row:
                if element < 0:
                    count += 1
        
        return count
        