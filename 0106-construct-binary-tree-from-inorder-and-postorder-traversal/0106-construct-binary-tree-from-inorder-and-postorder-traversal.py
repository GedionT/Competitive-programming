# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return 
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        
        inord_idx = inorder.index(root_val) #o(n) ? amortized?
        
        root.right = self.buildTree(inorder[inord_idx+1:], postorder)
        root.left = self.buildTree(inorder[:inord_idx], postorder)
        
        
        return root
        
        
        
        