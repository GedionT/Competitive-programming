# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        paths = []
         
        return self.dfs(root, [], targetSum)
    
    
    def dfs(self, node, path, targetSum):
        
        if node:
            
            # recurence relation
            path.append(node.val)
            
            # base case
            if not node.left and not node.right:
                if sum(path.copy()) == targetSum:
                    return True
            
            return self.dfs(node.left, path.copy(), targetSum) or self.dfs(node.right, path.copy(), targetSum)
        
       
        # #######  #

        # done without list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        _sum = 0
         
        return self.dfs(root, _sum, targetSum)
    
    
    def dfs(self, node, _sum, targetSum):
        
        if node:
            
            # recurence relation
            _sum += node.val
            
            # base case
            if not node.left and not node.right:
                if _sum == targetSum:
                    return True
            
            return self.dfs(node.left, _sum, targetSum) or self.dfs(node.right, _sum, targetSum)
        
       
        