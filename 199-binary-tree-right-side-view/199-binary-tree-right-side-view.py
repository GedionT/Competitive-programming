# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        level = deque([root])
        res = []
        
        while level:
            
            size = len(level)
            temp = []
            
            for i in range(size):
                
                curr = level.popleft()
                
                if not curr:
                    continue 
                    
                temp.append(curr.val)
                
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
                    
            if temp:    
                res.append(temp[-1])
        
        return res
            
            
           