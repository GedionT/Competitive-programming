# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        res = []
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
                
        dfs(root)
        
        res.sort()
        
        self.idx = 0
        
        def fix(root):
            if not root:
                return
            
            fix(root.left)
            if root.val != res[self.idx]:
                root.val = res[self.idx]
                self.idx += 1
            else:
                self.idx += 1
            fix(root.right)
            
        fix(root)
        