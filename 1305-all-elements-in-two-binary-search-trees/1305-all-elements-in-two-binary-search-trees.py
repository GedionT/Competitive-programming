# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        res = []
        
        def dfsInOrder(root):
            if not root:
                return
            
            if root.left:
                dfsInOrder(root.left)
            
            res.append(root.val)
            
            if root.right:
                dfsInOrder(root.right)
        
        
        dfsInOrder(root1)
        dfsInOrder(root2)
        
        return sorted(res)
                