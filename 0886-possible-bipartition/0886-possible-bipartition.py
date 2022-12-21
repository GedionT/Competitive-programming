class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color_group = [ -1 for i in range(n+1) ]
        
        # build graph or pass dislike to subroutine
        graph = defaultdict(list)
        
        for s,d in dislikes:
            graph[s].append(d)
            graph[d].append(s)
            
        # sub routine to handle disjoint graph
        for i in range(n):
            if color_group[i] == -1:
                if not self.isBipartiteUtil(graph, i, color_group):
                    return False
        return True
    
    def isBipartiteUtil(self, graph, node, color_group):
        color_group[node] = 1
        
        print(color_group)
        # create queue and append curr node for bfs traversal
        queue = deque()
        
        queue.append(node)
        
        # run while nodes in queue like bfs
        while queue:
            curr = queue.popleft()
            
            # break if self-loop found
            if curr in graph[curr]:
                return False
            
            # find all uncolored adjencent nodes
            for neigb in graph[curr]:
                if color_group[neigb] == -1:
                    color_group[neigb] = 1 - color_group[curr]
                    queue.append(neigb)
                    
                # return False if same color neigbour    
                elif color_group[neigb]  == color_group[curr]:
                    return False
        
        # processed all nodes properly
        return True