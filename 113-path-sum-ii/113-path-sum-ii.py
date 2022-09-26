# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
            5 4 11 2, 5 8 4 5 - backtracking
        """
        
        self.res = []
        self.dfs(root, targetSum, 0, [])
        return self.res
    
    
    def dfs(self, root: TreeNode, target: int, prev_sum: int, path_list: list):
        # base case
        if not root:
            return

        prev_sum += root.val
        path_list.append(root.val)

        if prev_sum == target and root.left == None and root.right == None:
            self.res.append(path_list[:])


        self.dfs(root.left, target, prev_sum, path_list)
        self.dfs(root.right, target, prev_sum, path_list)

        path_list.pop()


