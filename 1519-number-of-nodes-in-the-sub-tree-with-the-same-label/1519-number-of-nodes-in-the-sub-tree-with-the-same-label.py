class Solution:
        
    def dfs(self, node, parent, graph, count, res, labels):
        idx = ord(labels[node]) - ord('a')
        previous = count[idx]
        count[idx] += 1

        for neighb in graph[node]:
            if neighb != parent:
                self.dfs(neighb, node, graph, count, res, labels)

        res[node] = count[idx] - previous
            
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = [[] for _ in range(n)]
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        count = [0] * 26
        res = [0] * n
        
        self.dfs(0, -1, graph, count, res, labels)
        
        return res