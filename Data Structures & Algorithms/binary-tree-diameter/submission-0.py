# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
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

