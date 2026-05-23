"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        stack = [node]

        old_to_new[node] = Node(val=node.val)

        while stack:
            curr = stack.pop()
            curr_copy = old_to_new[curr]


            for ngbr in curr.neighbors:
                if ngbr not in old_to_new:
                    old_to_new[ngbr] = Node(val=ngbr.val)
                    stack.append(ngbr)

                curr_copy.neighbors.append(old_to_new[ngbr])


        return old_to_new[node]
