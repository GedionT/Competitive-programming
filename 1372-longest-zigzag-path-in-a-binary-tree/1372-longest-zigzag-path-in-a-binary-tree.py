# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # @ my approach
        # from every node run dfs with left and right alternative
        # each node should start with left and then right and save max
        
        maxPath = [0]
        
        def dfs(node, L, steps):
            if node:
                maxPath[0] = max(maxPath[0], steps)
                
                if L:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                    
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)
                    
        dfs(root, False, 0)
        dfs(root, True, 0)
        return maxPath[0]
    