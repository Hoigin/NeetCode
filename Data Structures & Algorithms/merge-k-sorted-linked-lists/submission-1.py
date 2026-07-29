# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        heap = []
        count = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, count, l))
                count += 1
        while heap:
            popval, count, pop = heapq.heappop(heap)
            if pop.next:
                heapq.heappush(heap, (pop.next.val, count, pop.next))
            curr.next = pop
            curr = curr.next
        return dummy.next