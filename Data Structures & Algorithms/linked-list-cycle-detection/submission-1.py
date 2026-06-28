# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
           return False
        
        curr = head
        map = {}
        i = 0
        while curr:
            if curr in map:
                return True
            else:
                map[curr] = i
            curr = curr.next
        return False