class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        for g in grid:
            
            left = 0
            right = len(g)-1
            
            while left <= right:
                mid = left + (right - left) // 2

                if g[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            
            ans += len(g) - left   
  
            
        return ans