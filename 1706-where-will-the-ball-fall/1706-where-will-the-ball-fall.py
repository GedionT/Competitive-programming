class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        def hasStuckDfs(row, col):   
            if row >= len(grid):
                return col
            
            if grid[row][col]==1 and col+1 < len(grid[0]) and grid[row][col+1]==1:
                return hasStuckDfs(row+1,col+1)
            
            elif grid[row][col]==-1 and col-1>=0 and grid[row][col-1]==-1:
                return hasStuckDfs(row+1,col-1)
            
            elif grid[row][col]==1 and col+1>=len(grid[0]):
                return -1
            
            else:
                return -1
                
        res = []   
        for ball in range(len(grid[0])):
            res.append(hasStuckDfs(0, ball))
        return res