# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        path = []

        def dfs(root):
            if not root:
                return []

            path.append(root.val)

            if root.left:
                dfs(root.left)

            if root.right:
                dfs(root.right)

            return path

        return dfs(root)
