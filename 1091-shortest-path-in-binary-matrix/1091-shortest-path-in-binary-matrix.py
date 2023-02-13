class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        queue = deque([(0,0,1)])

        if grid[0][0] == 1: return -1 


        while queue:
            x, y, steps = queue.popleft()
            
            if x == row-1 and y == col-1:
                return steps
            
            for nx,ny in [[x+1,y+1], [x-1,y-1], [x+1,y-1], [x-1,y+1], [x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
                if 0<=nx<row and 0<=ny<col and grid[nx][ny] == 0:
                    grid[nx][ny] = "X"
                    queue.append((nx, ny, steps+1))

        return -1