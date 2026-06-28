# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        curr1 = list1
        curr2 = list2
        res = ListNode(0)
        tail = res

        while(curr1 and curr2 ):
            if curr1.val <= curr2.val:
               tail.next = curr1
               curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        while curr1:
            tail.next = curr1
            curr1 = curr1.next
            tail= tail.next
        while curr2:
            tail.next = curr2
            curr2 = curr2.next
            tail = tail.next
        return res.next

               