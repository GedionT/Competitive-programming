# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left, right = root.left, root.right
        lh, rh = 1, 1    
        
        while left  : left,  lh = left.left,   lh+1           # each subtree by going all way down to
        while right : right, rh = right.right, rh+1           # the left and right (in logN time)

        if lh == rh : return ( 1 << lh ) - 1                         # if it's a full tree size is known
        
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)   
           
        
            