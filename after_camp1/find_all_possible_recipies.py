from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        
        
        """
        
            build adjecency list for recip -> ingridient 
                sandwich = bread, meat
                bread = yeast, flour
              
            
            for each adj list pick the one with no incoming edge by first counting
                if recip -> ingri in supplies
                    add to ans
                    
            while queue
                check for remaining adj list existence in supplies or ans
                    if yes: add to ans
                    if not: pass
            
            return ans
        
        """
        
        incoming = [0] * len(recipes)
        queue = deque()
        ans = []
        
        adj = defaultdict()
        
        for i in range(len(recipes)):
            adj[i] = ingredients[i]
            

            for item in adj[i]:
                count = 0
                if item in recipes:
                    count += 1
                adj[i].append(count)

        for i in range(len(recipes)):
            if recipes[i] in supplies:
                incoming[i] = 1
                queue.append(recipes[i])

        while queue:
            curr = queue.popleft()
            if curr in supplies:
                ans.append(curr)
                
            for i in range(len(recipes)):
                if recipes[i] in adj[curr]:
                    incoming[i] += adj[curr][recipes[i]]
                    if incoming[i] == 2:
                        queue.append(recipes[i])
                        incoming[i] = 0
        return ans

        
        
                    
                
        
            
         
    
        
        