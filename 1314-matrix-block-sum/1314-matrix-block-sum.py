class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        prefixSum = [ row[:] for row in mat ]
        
        for row in prefixSum:
            for i in range(1, len(row)):
                row[i] += row[ i-1 ]
                
        row = len(mat)
        col = len(mat[0])
        
        ans = [[0]*col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                
                top = max(0, i-k)
                bottom = min(i+k, row-1)
                
                for l in range(top, bottom+1):
                    
                    p_row = prefixSum[l]
                    
                    r_end = min(col-1, j+k)
                    l_end = max(0, j-k)
                    
                    if l_end:
                        ans[i][j] += p_row[r_end] - p_row[l_end - 1]
                    else:
                        ans[i][j] += p_row[r_end]
                        
        return ans