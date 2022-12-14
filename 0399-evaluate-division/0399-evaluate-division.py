class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # build graph
        graph = defaultdict(list)
        
        for idx in range(len(equations)):
            src, dest = equations[idx]
            weight = values[idx]
            
            graph[src].append([dest, weight])
            graph[dest].append([src, 1/weight])
        
        # iterate on queries and do a dfs
        result = []
        for a, b in queries:
            result.append(self.dfs(a, b, set(), graph))
        
        # return the result
        return result
    
    
    def dfs(self, src, dest, visited, graph):
        if src not in graph or dest not in graph:
            return -1
        
        if src == dest:
            return 1.0
         
        visited.add(src)
        
        for node in graph[src]:
            if node[0] not in visited:
                ans = self.dfs(node[0], dest, visited, graph)
                if ans != -1.0:
                    return ans * node[1]
                
        return -1
        
        
        