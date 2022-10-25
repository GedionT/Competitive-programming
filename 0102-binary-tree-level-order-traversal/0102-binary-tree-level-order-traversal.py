# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case
        if not root:
            return
        
        queue = deque([root])
        levels = []
        
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                curr = queue.popleft()
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                level.append(curr.val)
            
            levels.append(level)
        
        return levels
        
        
        
                
                