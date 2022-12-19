class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)

        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        # return self.dfs(source, destination, graph, visited)
        
        seen = [False]*n
        seen[source] = True
        queue = deque([source])
        
        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)
                    
        return False