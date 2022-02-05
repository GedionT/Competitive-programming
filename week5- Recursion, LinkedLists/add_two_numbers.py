# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        head = res
        carry = 0
        
        while l1 or l2 or carry:
            v2 = l1.val if l1.val else 0
            v1 = l2.val if l2.val else 0
            _sum = v2 + v1 + carry
            carry = _sum // 10
            _sum = _sum % 10
            
            
            res.next = ListNode(_sum)
            res = res.next
            
            l1, l2 = l1.next, l2.next
            
        if l1:
            res.next = l1
        elif l2:
            res.next = l2
            
            
        return head.next
            
        
        