# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # recurse, return link, swap, attach to link, return new link
        if not head:
            return None
        
        if head and not head.next:
            return head
        
        else:
            link = self.swapPairs(head.next.next)
            tmp = head.next
            tmp.next = head
            head.next = link
            return tmp
        