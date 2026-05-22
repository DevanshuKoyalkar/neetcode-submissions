# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        two_curr = head

        while curr:
            curr = curr.next
            if two_curr and two_curr.next:
                two_curr = two_curr.next.next

                if curr == two_curr:
                    return True

        return False 