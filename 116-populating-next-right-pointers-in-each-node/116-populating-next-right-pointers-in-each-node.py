"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        queue = deque([root])
        # ans = []
        while queue:
            size = len(queue)
            
            level = []
            for i in range(size):
                curr = queue.popleft()
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                level.append(curr)
            
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            level[-1].next = None
   
        return root
                
        