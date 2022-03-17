class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        for g in grid:
            
            left = 0
            right, best = len(g)-1, len(g)
            
            while left <= right:
                mid = left + (right - left) // 2

                if g[mid] < 0:
                    right = mid - 1
                    best = min(best, mid)
                else:
                    left = mid + 1
            
            ans += len(g) - best
  
            
        return ans