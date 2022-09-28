class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixMatrix = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.prefixMatrix[i][j] = self.prefixMatrix[i][j-1] + matrix[i-1][j-1]
                
        for j in range(1, len(matrix[0])+1):
            for i in range(1, len(matrix)+1):
                self.prefixMatrix[i][j] += self.prefixMatrix[i-1][j] 
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefixMatrix[row2+1][col2+1] - self.prefixMatrix[row1][col2+1]) - (self.prefixMatrix[row2+1][col1] - self.prefixMatrix[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)