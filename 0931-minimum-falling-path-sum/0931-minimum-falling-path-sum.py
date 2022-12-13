class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        for r in range(len(matrix)-2, -1, -1):
            for c in range(len(matrix)):
                best = matrix[r+1][c]
                
                if c > 0:
                    best = min(best, matrix[r+1][c-1])
                if c + 1 < len(matrix):
                    best = min(best, matrix[r+1][c+1])
                    
                matrix[r][c] = matrix[r][c] + best
                
        return min(matrix[0])
        
       