# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        """    
                1, 
                2, 3
                4, 5, 6
                7

                2
                1, 3
        """
        
        if not root.left and not root.right:
            return root.val

        
        level = deque([root])
        last = []

        while level:

            for _ in range(len(level)):
                curr = level.popleft()


                if curr.left:
                    level.append(curr.left)

                if curr.right:
                    level.append(curr.right)

            lvl_value = [ l.val for l in level]
            
            if lvl_value:
                last.clear()
                last = [ *lvl_value ]

        return last[0]
        