class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        #build the graph
        graph = defaultdict(list)
        
        for i in range(len(parent)):
            graph[parent[i]].append(i)
         
        self.max = 0
        
        def dfs(node, parent):
            if not graph[node]:
                if parent == s[node]:
                    return 0
                return 1
            
            left = right = 0
            
            for child in graph[node]:
                if s[node] != s[child]:
                    left = max(left, dfs(child, s[node]))
                    if right < left:
                        right, left = left, right
                else:
                    dfs(child, s[node])
            
            self.max = max(self.max, (left+right))
            
            return max(left, right) + 1
    
            
                
        dfs(0, "")
        return self.max + 1