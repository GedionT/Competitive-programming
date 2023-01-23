class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indeg = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            indeg[dest] += 1
            
        queue = deque([])
        
        for i in range(len(indeg)):
            if indeg[i] == 0:
                queue.append(i)
                
        canTake = 0
        while queue:
            
            curr = queue.popleft()
            canTake += 1
            
            for node in graph[curr]:
                indeg[node] -= 1
                
                if indeg[node] == 0:
                    queue.append(node)
                    
        if canTake < len(graph):
            return False
        
        return True
        
        
        
        
        
        