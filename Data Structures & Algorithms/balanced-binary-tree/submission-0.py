# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def getHeight(node):
            nonlocal is_balanced
            if not node:
                return 0
            
            _left = getHeight(node.left)
            _right = getHeight(node.right)

            # print(node.val, _left, _right)
            if abs(_left - _right) > 1:
                is_balanced = False
            
            return 1 + max(_left, _right)
        
        getHeight(root)
        return is_balanced