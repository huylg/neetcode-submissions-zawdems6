# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        temp = result

        while list1 is not None or list2 is not None:
            if list1 is None or (list2 is not None and list2.val <= list1.val):
                temp.next = list2
                list2 = list2.next  # pyright: ignore[reportOptionalMemberAccess]
            else:
                temp.next = list1
                list1 = list1.next
            temp = temp.next

        return result.next
