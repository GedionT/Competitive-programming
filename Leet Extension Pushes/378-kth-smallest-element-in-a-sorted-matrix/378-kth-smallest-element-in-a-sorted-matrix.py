class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        index_map = []   
        holder = []
        
        for i in range(len(matrix)):
            heappush(holder, (matrix[i][0], i, 0))
        
        # print(holder)
        

        while k-1:
            tups = heappop(holder)
            k -= 1
            
            if tups[2]+1 < len(matrix):
                heappush(holder, (matrix[tups[1]][tups[2]+1], tups[1], tups[2]+1 ))
            
                
        ans = heappop(holder)
        
        return ans[0]
        