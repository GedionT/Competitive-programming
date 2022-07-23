# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #         do a fast, slow and count len of slow
        #         slow is the first half
        #         if odd
        #             start at the next element
        #         else
        # start at the current slow and reverse
        #          we then have :
        #
        #          a -> b -> c -> * | c -> b -> a
        #           compare the two half
        #           if they are the same, return True
        #           else return False

        # if head is None or head.next is None:
        #     return True

        slow = head
        fast = head

        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # compare the two half
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
