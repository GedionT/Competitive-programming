class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        graphX = defaultdict(list)
        graphY = defaultdict(list)
        for x,y in stones:
            graphX[x].append(y)
            graphY[y].append(x)
        
       
        connectedComponent = 0
        visited = set()
        
        for x,y in stones:
            ### if the current stone has not been visited, do a BFS from it.
            if (x,y) not in visited:
                q = deque([(x,y)])
                while q:
                    xo,yo = q.popleft()
                    
                    if (xo,yo) not in visited:
                        visited.add((xo,yo))
                        ### since we used two hash map to store the neighbors,
                        ### we need to get all the neighbors fron the current stone.
                        for neY in graphX[xo]:
                            q.append((xo,neY))
                        for neX in graphY[yo]:
                            q.append((neX,yo))
                ### we find another connected component
                connectedComponent += 1
        
        return len(stones)-connectedComponent