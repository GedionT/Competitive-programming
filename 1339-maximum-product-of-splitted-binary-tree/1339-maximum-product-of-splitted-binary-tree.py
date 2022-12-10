# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9+7
        
        def dfs_total(node):
            if not node:
                return 0
            
            return node.val + dfs_total(node.left) + dfs_total(node.right)
        
        t = dfs_total(root)
        self.best = 0
        
        def dfs(node):
            if not node: return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            self.best = max(self.best, (t-l)*l, (t-r)*r)
            
            return node.val + l + r
            
        dfs(root)
        return self.best % MOD
            
            
        