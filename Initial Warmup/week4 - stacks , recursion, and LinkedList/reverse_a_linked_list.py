# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # iterative solution

        prev = None

        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev

        # recursive approach

#          # If head is empty or has reached the list end
#         if head is None or head.next is None:
#             return head

#         # Reverse the rest list
#         rest = self.reverseList(head.next)

#         # Put first element at the end
#         head.next.next = head
#         head.next = None

#         # Fix the header pointer
#         return rest
