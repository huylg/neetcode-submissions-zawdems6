# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        low = head
        hi = head.next


        while hi != low:
            if hi:
                hi = hi.next
            if hi:
                hi = hi.next
            low = low.next

        return hi is not None
