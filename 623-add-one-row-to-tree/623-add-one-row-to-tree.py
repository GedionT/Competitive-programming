# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        q = deque([root])
        dep = 1
        
        while dep != depth-1:   
            size = len(q)
            for i in range(size):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)          
            dep+=1
          
                
        for _ in range(len(q)):
            node = q.popleft()
            
            left = node.left
            right = node.right
            
            newLeft = TreeNode(val)
            newRight = TreeNode(val)
            
            node.left = newLeft
            newLeft.left = left
            
            node.right = newRight
            newRight.right = right
            
        return root