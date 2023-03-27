class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ROW = len(grid)
        COL = len(grid[0])
        
        directions = [(1,0), (0,1)]
        isvalid = lambda x, y: 0 <= x < ROW and 0 <= y < COL 
                
        @cache
        def dfs(x, y):
            if x == ROW-1 and y == COL-1:
                return grid[x][y]
            
            paths = []
            for xi, yi in directions:
                x2, y2 = x + xi, y + yi
                
                if isvalid(x2, y2):
                    paths.append(dfs(x2, y2))
                    
            return grid[x][y] + min(paths)
                    
            
        return dfs(0,0)
        
         