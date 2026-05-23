# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        result_head, result_tail = None, None

        while head1 or head2:
            min_node = None

            min_node = head1 if head1 and (not head2 or head1.val <= head2.val) else head2
            
            if not result_head:
                result_head = result_tail = min_node
            else:
                result_tail.next = min_node
                result_tail = min_node

            if min_node == head1:
                head1 = head1.next
            else:
                head2 = head2.next
        
        return result_head