# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        

        """
        You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. 
        There are n coins in total throughout the whole tree.

        In one move, we may choose two adjacent nodes and move one coin from one node to another. 
        A move may be from parent to child, or from child to parent.

        Return the minimum number of moves required to make every node have exactly one coin.

        """
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.ans += abs(left) + abs(right)
            
            return root.val + left + right - 1
        
        self.ans = 0
        dfs(root)
        return self.ans