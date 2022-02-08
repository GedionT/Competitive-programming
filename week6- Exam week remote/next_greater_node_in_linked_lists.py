# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    
        stack = []
        
#         collect values in the linked list
        while head:
            stack.append(head.val)
            head = head.next
        
        temp = []
        
        i = len(stack) - 1
        
#         create answer list
        res = [0] * len(stack)
        
        while stack:
            curr = stack.pop()
            while temp:
                if temp[-1] > curr:
                    res[i] = temp[-1]
                    temp.append(curr)
                    break
                temp.pop()
            if not temp:
                temp.append(curr)
                res[i] = 0
            i -= 1
   
        return res
                
            