# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that sits before the head
        dummy = ListNode(0, head)
        start = end = dummy

        for _ in range(n):
            end = end.next
        
        while end and end.next:
            start = start.next
            end = end.next

        # we don't mind where start is
        start.next = start.next.next
        
        return dummy.next