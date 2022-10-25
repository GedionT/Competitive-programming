# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max = 0
    
        def findDiameter(node):
            # handle base case
            if not node:
                return 0
            
            left = findDiameter(node.left)
            right = findDiameter(node.right)
            
            self.max = max(self.max, left+right)
            
            return max(left,right)+1
        
        
        
        findDiameter(root)
        return self.max
        