# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # move by the fast, slow in window of size of n
        # when fast ends, map the slow to the end of fast(next ptr)
        
        if not head.next:
            return None
        
        dummy = ListNode(0, head)
        
#         dummy.next = head
    
        # head = dummy
        fast = dummy
        slow = dummy
        
        # move fast according to n
        while n > 0 and fast.next:
            fast = fast.next
            n -= 1
            
       # we've setup the pointers to move in between len of n
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        if slow.next == fast:
            slow.next = None
        else:
            slow.next = slow.next.next
        
            
        return dummy.next