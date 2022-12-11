# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max = -sys.maxsize - 1
        
        
        def dfs(root):
            if not root:
                return 0
            
            left = max(dfs(root.left), 0) # accomodate -ve bc zero can replace as not pick
            right = max(dfs(root.right), 0)
            
            self.max = max(self.max, left + root.val + right)
            
            return max(left+root.val, right+root.val)
        
        dfs(root)
        return self.max