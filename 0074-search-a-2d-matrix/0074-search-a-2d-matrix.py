class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        find_val = lambda x, y: x*m+y
        find_cord = lambda x: (x//m, x%m)
        
        l, r = 0, find_val(len(matrix)-1, len(matrix[0])-1)
        
        while l <= r:
            mid = (l+r)//2
            coord = find_cord(mid)
            
            if target == matrix[coord[0]][coord[1]]:
                return True
                
            elif target < matrix[coord[0]][coord[1]]:
                r = mid-1
            else:
                l = mid+1
            
        
        return False
            
            
                
            
        