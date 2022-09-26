# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return 
        
        queue = deque([(root)])
        
        res = []
        
        while queue:
            l = len(queue)
            path = []
            
            for i in range(l):
                curr = queue.popleft()
                path.append(curr.val)
                if curr.left:
                    queue.append((curr.left))
                if curr.right:
                    queue.append((curr.right))

            res.append(path)
        return res