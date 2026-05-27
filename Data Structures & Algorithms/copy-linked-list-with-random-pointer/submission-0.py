"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}


        curr = head
        result_head = result_tail = None

        while curr:
            node = None

            if curr in old_to_new:
                node = old_to_new[curr]
            else:
                node = Node(curr.val)

            if not result_tail:
                result_head = result_tail = node
            else:
                result_tail.next = node
                result_tail = node
            
            old_to_new[curr] = node

            # handle random pointer
            new_random = None
            if curr.random in old_to_new:
                new_random = old_to_new[curr.random]
            else:
                if curr.random:
                    new_random = Node(curr.random.val)
                
                old_to_new[curr.random] = new_random
            
            node.random = new_random

            # move curr
            curr = curr.next
        
        return result_head




