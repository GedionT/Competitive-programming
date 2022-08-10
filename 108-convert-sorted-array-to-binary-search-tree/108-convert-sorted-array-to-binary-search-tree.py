# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = math.ceil((len(nums) + 1 )/ 2) - 1
        
        root = TreeNode(nums[mid])
        
        def bst(numms, parent):
            if len(numms) == 0:
                return None
            
            mid = math.ceil((len(numms) + 1 )/ 2) - 1
            temp = TreeNode(numms[mid])
            
            temp.left = bst(numms[:mid], temp)
            temp.right = bst(numms[mid+1:], temp)
            
            
            return temp
        
        root.left = bst(nums[:mid], root)
        root.right = bst(nums[mid+1:], root)
        
        return root