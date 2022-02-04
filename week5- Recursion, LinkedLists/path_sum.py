# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        paths = []

        return self.dfs(root, [], targetSum)

    def dfs(self, node: Optional[TreeNode], path: List, targetSum: int) -> bool:

        if node:

            # recurrence relation
            path.append(node.val)

            # base case
            if not node.left and not node.right:
                if sum(path.copy()) == targetSum:
                    return True

            return self.dfs(node.left, path.copy(), targetSum) or self.dfs(node.right, path.copy(), targetSum)


if __name__ == "__main__":

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
