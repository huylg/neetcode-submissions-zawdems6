# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lo = None
        hi = head

        while hi is not None:
            temp = hi.next
            hi.next = lo
            lo = hi
            hi = temp

        return lo
