# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
       
        first = head
        second = head.next.next
        
        while second and second.next:
            first = first.next
            second = second.next.next
            
        first.next = first.next.next
        
        return head
