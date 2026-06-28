# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0 :
           return head

        # Find the length of the linked-list
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        
        if length == 1:
            return None
        if length == 2:
            curr = head
            next_node = curr.next 
            if n == 1:
                return curr
            else:
                return next_node
        # Find the index to delete
        idx = length - n 
        dummy = head
        prev = None
        curr = head
        while curr:
            if idx == 0:
                prev.next = curr.next
                break
            idx -= 1
            prev = curr
            curr = curr.next
        return dummy 


