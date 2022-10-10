# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.inter = 0
        
        def dfs(root):  
            if not root: 
                return 
            
            dfs(root.right)
            
            root.val += self.inter
            self.inter = root.val
            
            dfs(root.left)
            
            return root
            
        return dfs(root)
        
        