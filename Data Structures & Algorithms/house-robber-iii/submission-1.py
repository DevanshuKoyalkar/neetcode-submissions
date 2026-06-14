# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        stack = [root]
        node_map = {None: (0,0)}

        while stack:
            node = stack[-1]
            if node.left and node.left not in node_map:
                stack.append(node.left)
            elif node.right and node.right not in node_map:
                stack.append(node.right)
            else:
                stack.pop()

                left_select, left_not_select = node_map[node.left]
                right_select, right_not_select = node_map[node.right]

                node_select = node.val + left_not_select + right_not_select
                node_not_select = max(left_select, left_not_select) + max(right_select, right_not_select)

                node_map[node] = (node_select, node_not_select)
        
        return max(node_map[root])


    def rob2(self, root: Optional[TreeNode]) -> int:
        '''

        at each node store two values --> max if selected, max if not selected 
        '''

        def helper(node):
            if not node:
                return 0, 0
            
            left_select, left_not_select = helper(node.left)
            right_select, right_not_select = helper(node.right)
            
            node_select = node.val + left_not_select + right_not_select
            node_not_select = max(left_select, left_not_select) + max(right_select, right_not_select)

            return node_select, node_not_select
        
        return max(helper(root))