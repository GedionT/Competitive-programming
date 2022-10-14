# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        dummy = ListNode()
        dummy.next = head
        
        first = dummy
        second = dummy
        
        while second and second.next is not None and second.next.next:
            first = first.next
            second = second.next.next
            
        first.next = first.next.next
        
        return head
