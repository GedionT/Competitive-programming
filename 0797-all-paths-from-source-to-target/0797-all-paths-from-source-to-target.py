class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        visited = set()
        self.paths = []
        
        return self.dfs(n, 0, graph, visited, [])
         

    def dfs(self, n, node, graph, visited, path):
        if node == n:
            self.paths.append(path[:])
            return

        if node not in visited:
            path.append(node)

        for neigb in graph[node]:
            visited.add(neigb)
            path.append(neigb)
            self.dfs(n, neigb, graph, visited, path)
            visited.remove(neigb)
            path.pop()

        return self.paths