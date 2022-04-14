class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        indegree = {}
        
        
        for i in range(numCourses):
            graph[i] = []
            indegree[i] = 0
            
        
        for edge in prerequisites:
            child = edge[0]
            parent = edge[1]
            
            indegree[child] += 1
            graph[parent].append(child)
            
            
        sources = deque()
        
        for i,j in indegree.items():
            if j==0:
                sources.append(i)
        ans=[]
        
        while sources:
            c = sources.popleft()
            ans.append(c)
            
            for nbr in graph[c]:
                indegree[nbr] -= 1
                
                if indegree[nbr] == 0:
                    sources.append(nbr)
        
        if len(ans) == numCourses:
            return True
        return False