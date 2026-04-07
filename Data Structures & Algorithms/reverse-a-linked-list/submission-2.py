# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        lo = head
        hi = head.next

        while hi is not None:
            temp = hi.next
            hi.next = lo
            lo = hi
            hi = temp

        head.next = None
        return lo
