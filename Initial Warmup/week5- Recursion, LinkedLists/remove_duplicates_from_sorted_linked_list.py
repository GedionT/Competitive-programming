# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        unique = head
        
        while head and head.next:
            if head.val == head.next.val:
                if head.next.next:
                    head.next.val = head.next.next.val
                    head.next = head.next.next
                else:
                    head.next = None
            else:
                head = head.next
                
        return unique
        