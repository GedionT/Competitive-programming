# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level = deque([root])
        if not root:
            return []
        
        zigzag_order = [[root.val]] 
        flag = True
        
        while level:
            size = len(level)
            
            for i in range(size):
                current = level.popleft()
            
                if current:
                    level.append(current.left)
                    level.append(current.right)    
                else:
                    continue
                # gets every level in a list 

            # extract every val in level if not null
            level_vals = [ l.val for l in level if l ]
     
                    
            if len(level_vals) > 0:
                if flag:
                    zigzag_order.append(reversed(level_vals))
                    flag = False
                else:
                    zigzag_order.append(level_vals)
                    flag = True

        return zigzag_order