# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        levels = defaultdict(list, {0: [root.val]})
        
        def dfs(node, level):
            if not node:
                return
            
            if node.left:
                levels[level + 1].append(node.left.val)
                dfs(node.left, level + 1)
            if node.right:
                levels[level + 1].append(node.right.val)
                dfs(node.right, level + 1)
        
        dfs(root, 0)
        
        return levels.values()
                