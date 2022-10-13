class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bin_search(target, mat):
            l, r = 0, len(mat)-1
            
            while l <= r:
                mid = l + (r - l) // 2

                if target > mat[mid][0]:
                    l = mid+1
                elif target < mat[mid][0]:
                    r = mid-1 
                else:
                    return True
                    
                    
            sub = mat[r]
            l, r = 0, len(sub)-1
            
            while l <= r:
                mid = l + (r - l) // 2
                
                if target == sub[mid]:
                    return True
                elif target < sub[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return False

        
        ans = bin_search(target, matrix)

        return ans