class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # one liner in-efficient code O(n)
        return [ True for rows in range(len(matrix)) for cols in range(len(matrix[0])) if matrix[rows][cols] == target ]
        
        # expanded inefficient O(n) 
        # for rows in range(len(matrix)):
        #     for cols in range(len(matrix[0])):
        #         if matrix[rows][cols] == target:
        #             return True
        # return False
                    
                
                
                
#                 row_start = col_start = 0
#                 row_len, col_len = len(matrix), len(matrix[0])

#                 while row_start <= row_len:
#                     mid = row_start + row_len // 2
                    
#                     if row[mid] <= target:
#                         row_start = mid + 1
#                         result = mid

#                     else:
#                         row_len = mid-1