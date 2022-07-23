class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]
        rank = [1 for i in range(len(isConnected))]
        count = len(isConnected)
        
        def find(x):
            if x == parents[x]:
                return x
            parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    parents[rooty] = rootx
                elif rank[rootx] < rank[rooty]:
                    parents[rootx] = rooty
                else:
                    parents[rooty] = rootx
                    rank[rootx] += 1
                nonlocal count 
                count -= 1
        
        def connecte(x,y):
            return find(x) == find(y)
        
        
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union(i,j)
                    
                    
        return count
                    
                    
        
                    
        
        
        