
 # Definition for a binary tree node.
from typing import Deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bfs_tree(self, root: 'TreeNode') -> 'TreeNode':
            
            queue = Deque([root])
            visited = []
            
            while queue:
                new = queue.popleft()
                visited.append(new.val)
                
                if new.left:
                    queue.append(new.left)
                if new.right:
                    queue.append(new.right)
                
            
            print(visited)
