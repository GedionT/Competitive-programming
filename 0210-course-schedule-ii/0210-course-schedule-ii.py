class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
                        
        queue = deque([])
        
        for node in range(len(indegree)):
            if indegree[node] == 0:
                queue.append(node)
                
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            for node in graph[curr]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
                    
        if len(order) != numCourses:
            return []
        
        return order