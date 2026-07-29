# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        while heap:
            popval, i, pop = heapq.heappop(heap)
            if pop.next:
                heapq.heappush(heap, (pop.next.val, i, pop.next))
            curr.next = pop
            curr = curr.next
        return dummy.next