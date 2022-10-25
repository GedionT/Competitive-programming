# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max = 0
        
        def countDiameter(root):
            # handle base case
            if not root:
                return 0
            
            
            left = countDiameter(root.left)
            right = countDiameter(root.right)
            
            self.max = max(self.max, (right + left))
            
            return max(left, right) + 1
        
        
        countDiameter(root)
        
        return self.max