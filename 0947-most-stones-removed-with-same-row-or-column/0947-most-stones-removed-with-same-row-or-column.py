class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        graphX = defaultdict(list)
        graphY = defaultdict(list)
        
        for x,y in stones:
            graphX[x].append(y)
            graphY[y].append(x)
            
        visited = set()
        
        def dfs(xo,yo):
            if (xo,yo) not in visited:
                visited.add((xo,yo))
                for nebY in graphX[xo]:
                    dfs(xo,nebY)
                for nebX in graphY[yo]:
                    dfs(nebX,yo)
        
        connectedComponent = 0
        
        for x,y in stones:
            if (x,y) not in visited:
                dfs(x,y)
                connectedComponent += 1
        
        return len(stones)-connectedComponent