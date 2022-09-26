# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        level = deque([root])
        
        res = []
        
        while level:
            
            next_level = []
            
            level_sum = count = 0
            for node in level:
                
                if not node:
                    continue
                
                level_sum += node.val
                
               
                next_level.append(node.left)
                next_level.append(node.right)
                
                count += 1
            
            if count:
                res.append(level_sum/count)
                
            level = next_level
        
        return res
            
        
        