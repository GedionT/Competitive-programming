class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # edge case
        if n <= 2:
            return [i for i in range(n)]
        
        # build graph and count indegree
        graph = [ set() for i in range(n) ]
        
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)

        # add leaves to queue
        leaves = []
        
        for node in range(n):
            if len(graph[node]) == 1:
                leaves.append(node)
                
        # trim leaves until reaching centroid 2 nodes (n is rem_nodes)
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            
            while leaves:
                curr = leaves.pop()
                
                neighbor = graph[curr].pop()
                graph[neighbor].remove(curr)
                
                if len(graph[neighbor]) == 1:
                        new_leaves.append(neighbor)
            
            leaves = new_leaves
            
        return leaves  # centroids
            
        
            
        