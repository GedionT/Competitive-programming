class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        
        # Create a 2D table to store the minimum path sum for each cell
        dp = [[0] * COL for _ in range(ROW)]
        
        # Initialize the bottom-right corner of the table
        dp[ROW-1][COL-1] = grid[ROW-1][COL-1]
        
        # Initialize the bottom row of the table
        for j in range(COL-2, -1, -1):
            dp[ROW-1][j] = dp[ROW-1][j+1] + grid[ROW-1][j]
        
        # Initialize the rightmost column of the table
        for i in range(ROW-2, -1, -1):
            dp[i][COL-1] = dp[i+1][COL-1] + grid[i][COL-1]
        
        # Compute the minimum path sum for each cell starting from the second-to-last row and column
        for i in range(ROW-2, -1, -1):
            for j in range(COL-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        
        # Return the minimum path sum for the top-left corner of the grid
        return dp[0][0]
