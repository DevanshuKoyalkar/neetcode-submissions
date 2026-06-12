# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        stack = [root]
        heights = {None: 0}
        is_balanced = True

        while stack:
            node = stack[-1]

            if node.left and node.left not in heights:
                stack.append(node.left)
            elif node.right and node.right not in heights:
                stack.append(node.right)
            else: # process node only after its children processed
                stack.pop()
                left_h = heights[node.left]
                right_h = heights[node.right]

                if abs(left_h - right_h) > 1:
                    return False
                
                heights[node] = 1 + max(left_h, right_h)
        
        return True


    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
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