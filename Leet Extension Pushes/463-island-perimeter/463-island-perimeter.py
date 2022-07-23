class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        def inBound(x,y): 
            return 0<=x<len(grid) and 0<=y<len(grid[0])
        
        perimeter = 0
        
        def dfs(i,j):
            nonlocal perimeter
            visited.add((i,j))
            ne_count = 0
            for dx,dy in directions:
                nx,ny = i + dx,j +dy
                if inBound(nx,ny) and (nx,ny) not in visited and grid[nx][ny]== 1:
                    dfs(nx,ny)
                    
                if inBound(nx,ny) and grid[nx][ny]== 1:
                    ne_count += 1
                    
            perimeter += 4 - ne_count
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    
        return perimeter