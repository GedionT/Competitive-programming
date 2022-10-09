# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        res = []
        
        def dfs(root):  
            if not root:
                return
            
            if root.left:
                dfs(root.left)
        
            res.append(root.val)
            
            if root.right:
                dfs(root.right)
        
        dfs(root)
        
        l, r = 0, len(res)-1
        
        while l < r:
            
            if res[l] + res[r] < k:
                l += 1
            elif res[l] + res[r] > k:
                r -= 1
            else:
                return True
        
        return False
            