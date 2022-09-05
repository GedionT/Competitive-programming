"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        d = defaultdict(list)
        
        def dfs(node, level):
            if not node: return
            
            d[level].append(node.val)
            
            for child in node.children:
                if child:
                    dfs(child, level+1)
            
        dfs(root, 0)    
        return [ d[i] for i in d ] 
            