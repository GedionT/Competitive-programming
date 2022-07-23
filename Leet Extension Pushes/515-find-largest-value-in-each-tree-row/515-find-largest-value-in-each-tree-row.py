# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        # TODO: handle edge case 
        if not root:
            return 
         
        level = deque([root])
        ans, temp = [], []
    
        while level:
            size = len(level)
            for i in range(size):
                curr = level.popleft()
                
                temp.append(curr.val)
                
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
                    
            ans.append(max(temp))
            temp = []
            
        return ans
        