from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # one way is to use union find and find abs root 
        # if same return true else false
        
        # using dfs below
        
        # space O(3n)=O(n)
        # time O(n)
        
        adj_list = defaultdict(list)
        
        
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
            
            
        visited = set()
        
        
        def dfs(node):
            
            if node == destination: # means there is path and arrives at dest
                return True
            
            
            if node not in visited:
                visited.add(node)
                
                for neighbour in adj_list[node]:
                    result = dfs(neighbour)
                    
                    if result:
                        return True
                    
                    
        return dfs(source)
            
            