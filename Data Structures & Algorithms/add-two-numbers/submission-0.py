# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ptr1, ptr2 = l1, l2
        result_head, result_tail = None, None

        while ptr1 or ptr2 or carry:
            current_sum = ptr1.val if ptr1 else 0 
            current_sum += ptr2.val if ptr2 else 0
            current_sum += carry

            current_sum, carry = current_sum % 10, current_sum // 10

            node = ListNode(current_sum)

            if not result_head:
                result_head = result_tail = node
            else:
                result_tail.next = node
                result_tail = node


            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

        return result_head