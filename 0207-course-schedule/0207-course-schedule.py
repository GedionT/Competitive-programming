class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1    
        
        queue = deque([])
        
        for idx in range(len(indegree)):
            if indegree[idx] == 0:
                queue.append(idx)
                
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            
            for node in graph[curr]:
                indegree[node] -= 1
                
                if indegree[node] == 0:
                    queue.append(node)
                    
        
        return count == numCourses
        
        
        