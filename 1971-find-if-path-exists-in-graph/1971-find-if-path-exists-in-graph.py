class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        visited = set()

        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        return self.dfs(source, destination, graph, visited)
        
    
    def dfs(self, node, dest, graph, visited):
        if node == dest:
            return True
        
        visited.add(node)
        
        for neigb in graph[node]:
            if neigb not in visited:
                hasPath = self.dfs(neigb, dest, graph, visited)
                if hasPath:
                    return True
                
        return False
        
        
        
        