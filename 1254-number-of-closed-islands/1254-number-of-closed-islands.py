class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        
        def dfs(r,c):
            if (r < 0 or c < 0 or
                r == rows or c == cols):
                return 0 # False
            
            if grid[r][c] == 1 or (r, c) in visited:
                return 1 # True
        
            visited.add((r,c))
            
            return min(dfs(r+1, c),
            dfs(r-1, c),
            dfs(r, c+1),
            dfs(r, c-1)
               )
            
            
        # loop through all grids and if it's land and not visited perform dfs
        count = 0
        for r in range(rows):
            for c in range(cols):
                if not grid[r][c] and (r,c) not in visited:
                    count += dfs(r, c)
                    
                    
        return count
        