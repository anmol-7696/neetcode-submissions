from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        dummy = ListNode(0)
        tail = dummy

        # Step 1: push FIRST node of each list
        for node in lists:
            if node:
                heappush(heap, (node.val, id(node), node))

        # Step 2: process heap
        while heap:
            val, _, node = heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heappush(heap, (node.next.val, id(node.next), node.next))

        return dummy.next

