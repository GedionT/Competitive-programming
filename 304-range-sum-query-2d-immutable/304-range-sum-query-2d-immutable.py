class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        Rows, Cols = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (Cols + 1) for r in range(Rows + 1)]
        
        # prefix sum
        for r in range(Rows):
            prefix = 0      # for every raw - calculate prefix sum
            for c in range(Cols):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1] # above row sum
                self.sumMat[r+1][c+1] = prefix + above

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1 # add offset to adjust the boundary 
        
        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1-1][c2]
        left = self.sumMat[r2][c1-1]
        topLeft = self.sumMat[r1-1][c1-1]
        
        return bottomRight - above - left + topLeft
                
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)