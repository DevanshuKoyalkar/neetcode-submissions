# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # base case
        if not head or not head.next:
            return

        slow_ptr = head
        fast_ptr = head

        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        first_chain = head
        second_chain = slow_ptr.next
        slow_ptr.next = None

        def reverse(node):
            curr = node
            prev = None

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
        
            return prev
    
        def interleave(list1, list2):
            ptr1, ptr2 = list1, list2
            while ptr2:
                tmp1, tmp2 = ptr1.next, ptr2.next

                ptr1.next = ptr2
                ptr2.next = tmp1

                ptr1 = tmp1
                ptr2 = tmp2
            

        reversed_second_chain = reverse(second_chain)
        interleave(first_chain, reversed_second_chain)
