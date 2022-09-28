class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        
        total = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    total += 1
                    grid[i][j] = '0'
                    q.append([i, j])
                    
                    while q:
                        point = q.popleft()
                        row = point[0]
                        col = point[1]
                        
                        if row-1>=0 and grid[row-1][col] == '1':
                            q.append([row-1, col])
                            grid[row-1][col] = '0'
                        if row+1< rows and grid[row+1][col] == '1':
                            q.append([row+1, col])
                            grid[row+1][col] = '0'
                        if col+1<cols and grid[row][col+1] == '1':
                            q.append([row, col+1])
                            grid[row][col+1] = '0'
                        if col-1 >= 0 and grid[row][col-1] == '1':
                            q.append([row, col-1])
                            grid[row][col-1] = '0'
                    
        return total