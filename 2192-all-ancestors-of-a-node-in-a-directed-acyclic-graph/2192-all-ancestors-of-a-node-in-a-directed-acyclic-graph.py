class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        
        indeg = [0] * n
        
        for src, dest in edges:
            graph[src].append(dest)
            indeg[dest] += 1
        
        queue = deque([])
        
        for node in range(len(indeg)):
            if indeg[node] == 0:
                queue.append(node)
                
        ans = [ set() for _ in range(n) ]
        
        while queue:
            node = queue.popleft()
            
            for neighb in graph[node]:
                #current node is ancestor to each and every neighboring node!
                ans[neighb].add(node)
                
                #every ancestor of current node is also an ancestor to the neighboring node!
                ans[neighb].update(ans[node])
                
                indeg[neighb] -= 1
                if indeg[neighb] == 0:
                    queue.append(neighb)
 
        ans = [(sorted(list(ancestor))) for ancestor in ans]
        return ans