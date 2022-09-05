"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        ans = []
        queue = deque([root]) 
        
        while queue:
            ans.append([ i.val for i in queue ])
            
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                
                for child in curr.children:
                    if child:
                        queue.append(child)
                        
    
        return ans