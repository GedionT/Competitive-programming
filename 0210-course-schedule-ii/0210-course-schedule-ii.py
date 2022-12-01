class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        # build the graph

        for i in range(numCourses):
            graph[i] = []
            
        for a, b in prerequisites:
            graph[b].append(a)
    
        order = []
        tracker = [0] * numCourses
        
        for g in range(len(graph)):
            hasCyc = self.hasCycle(g, tracker, graph, order)
            if hasCyc:
                return []
        
        return reversed(order)
        
        
    def hasCycle(self, node, tracker, graph, order):
        # no cycle
        if tracker[node] == 2:
            return False
        
        # has cycle
        if tracker[node] == 1:
            return True
        
        # if it's white, mark as gray (observed on path)
        tracker[node] = 1
        
        for neighbor in graph[node]:
            hasCycle = self.hasCycle(neighbor, tracker, graph, order)
            if hasCycle:
                return True
            
        tracker[node] = 2
        order.append(node)
        return False
        
        
        
        
        
        
        