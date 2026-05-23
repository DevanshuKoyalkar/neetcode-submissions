# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, _min, _max):
            if not root: 
                return True
            
            if root.val <= _min or root.val >= _max: 
                return False
            
            return helper(root.left, _min, root.val) and helper(root.right, root.val, _max)

        return helper(root, float('-inf'), float('inf'))