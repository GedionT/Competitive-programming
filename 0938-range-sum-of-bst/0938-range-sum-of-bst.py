# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        total = [0]
        
        def dfs(root):
            if not root:
                return 
            
            if root.left:
                dfs(root.left)
            
            if root.val >= low and root.val <= high:
                total[0] += root.val
                
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return total[0]