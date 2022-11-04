# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        res = []
        
        def dfs(root):
            if not root:
                return 0
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
            
         
        dfs(root)
        return len(res)
            
            
           
        
            