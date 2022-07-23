

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        size = 0
        counter = 0
        # save the head so we can traverse later
        temp = head

        # traverse the loop and find the length
        while temp:
            counter += 1
            temp = temp.next

        # find the median
        counter = counter//2
        temp = head

        # traverse from the start to the middle
        while size < counter:
            size += 1
            temp = temp.next

        # head points to the remaining middle out list
        head = temp

        return head

        """
        alternative approach
        TWO POINTER
        one moves with level two, the other with level one
        return the level of one when level of two reaches the end
        """
        # temp1 = head
        # temp2 = head

        # while temp2 != None and temp2.next != None:
        #     temp1 = temp1.next
        #     temp2 = temp2.next.next

        # return temp1


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    print(Solution().middleNode(head))
    print(Solution().middleNode(None))
    print(Solution().middleNode(ListNode(1)))
    print(Solution().middleNode(ListNode(1, ListNode(2))))
    print(Solution().middleNode(ListNode(1, ListNode(2, ListNode(3)))))
