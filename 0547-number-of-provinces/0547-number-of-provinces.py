class UnionFind:
    def __init__(self, n):
        self.root = [ i for i in range(n) ]
        self.rank = [1 for i in range(n) ]
        self.province = n 
        
    def find(self, x):
        if x == self.root[x]:
            return x

        x = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX]  > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                
            self.province -= 1  

 
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        
        uf = UnionFind(provinces)
        
        for i in range(provinces):
            for j in range(i+1, len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
                    
        return uf.province