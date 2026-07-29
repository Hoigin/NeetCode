# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2
        l1, l2 = list1, list2
        res = curr = ListNode()
        while l1 or l2:
            if l1.val <= l2.val:
                curr.next = l1
                if not l1.next:
                    curr = curr.next
                    curr.next = l2
                    break
                l1 = l1.next
            else:
                curr.next = l2
                if not l2.next:
                    curr = curr.next
                    curr.next = l1
                    break
                l2 = l2.next
            curr = curr.next
        return res.next