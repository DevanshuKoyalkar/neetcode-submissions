# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        stack = [root]
        heights = {None: 0}
        diameter = 0

        while stack:
            node = stack[-1]

            if node.left and node.left not in heights:
                stack.append(node.left)
            elif node.right and node.right not in heights:
                stack.append(node.right)
            else:
                stack.pop()
                left_h = heights[node.left]
                right_h = heights[node.right]

                diameter = max(diameter, left_h + right_h)
                heights[node] = 1 + max(left_h, right_h)
        
        return diameter


    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height_tree(node):
            nonlocal diameter
            if not node: 
                return 0
            if not node.left and not node.right:
                return 1

            left_height = height_tree(node.left)
            right_height = height_tree(node.right)

            diameter = max(diameter, left_height + right_height)
            return 1 + max(left_height, right_height)


        height_tree(root)
        return diameter

