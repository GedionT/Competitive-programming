class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        
        graph = defaultdict(set)
        indegree = defaultdict(int)
        ans = []
        
        for r in range(len(recipes)):
            graph[recipes[r]] = set(ingredients[r])
            indegree[recipes[r]] = len(ingredients[r])
            
        
        queue = deque()
        for val in supplies:
            queue.append(val)
        
        while queue:
            curr = queue.popleft()
            
            if curr in recipes :
                ans.append(curr)
                
            for g in graph:
                if curr in graph[g]:
                    indegree[g] -= 1
                    if indegree[g] == 0:
                        queue.append(g)
            
        
        return ans