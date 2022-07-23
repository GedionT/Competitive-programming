class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        use_memo = {}
        
        
        def dfs(i,j):
            if i == len(triangle):
                return 0
            
            if (i,j) in use_memo:
                return use_memo[(i,j)] 
            
            use_memo[(i,j)] = triangle[i][j] + min(dfs(i+1,j) , dfs(i+1,j+1))
            use_memo
            return use_memo[(i,j)]
        
       
        return dfs(0, 0)