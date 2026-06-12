# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        stack = [(root, float('-inf'), float('inf'))]
        visited = set()

        while stack:
            node, lower_bound, upper_bound = stack[-1]

            if node.left and node.left not in visited:
                stack.append((node.left, lower_bound, node.val))
            elif node.right and node.right not in visited:
                stack.append((node.right, node.val, upper_bound))
            else:
                stack.pop()
                visited.add(node)
                if node.val <= lower_bound or node.val >= upper_bound:
                    return False
            
        return True




    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        def helper(root, _min, _max):
            if not root: 
                return True
            
            if root.val <= _min or root.val > _max: 
                return False
            
            return helper(root.left, _min, root.val) and helper(root.right, root.val, _max)

        return helper(root, float('-inf'), float('inf'))