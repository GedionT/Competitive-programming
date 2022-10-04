# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        pathSum = 0
        return self.dfs(root, pathSum, targetSum)


    def dfs(self, node, pathSum, targetSum):

        if node:
            # recurence relation
            pathSum += node.val

            # base case
            if not node.left and not node.right:
                if pathSum == targetSum:
                    return True

            return self.dfs(node.left, pathSum, targetSum) or self.dfs(node.right, pathSum, targetSum)