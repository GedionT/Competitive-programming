# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        level = deque([root])
        
        res = []
        
        
        while level:
            size = len(level)
            
            temp = []
            for i in range(size):
                curr_node = level.popleft()
            
                if not curr_node:
                    continue
                
                temp.append(curr_node.val)
                
                if curr_node.left:
                    level.append(curr_node.left)
                if curr_node.right:
                    level.append(curr_node.right)
            
            if temp:
                res.append(temp)
        
        return reversed(res)