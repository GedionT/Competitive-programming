class Solution:
    def dfs(self, node, start, end, graph, order, visited):
        if node == end:
            order.append(node)
            return
        
        visited.add(node)
        order.append(node)

        for neigb in graph[node]:
            if neigb not in visited:
                self.dfs(neigb, start, end, graph, order, visited)

        return
    
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for frm, to in adjacentPairs:
            graph[frm].append(to)
            graph[to].append(frm)
            
        start = None
        end = None
        for node in graph:
            if not start and len(graph[node]) == 1:
                start = node
            elif start and len(graph[node]) == 1:
                end = node
            else:
                continue
        
        visited = set()
        order = []
        self.dfs(start, start, end, graph, order, visited)
        
        return order
    
        
        
        
            