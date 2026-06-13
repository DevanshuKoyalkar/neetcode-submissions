# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result

        stack = [] # actual call stack of the function
        curr = root

        while stack or curr:
            while curr: # travel to the leftmost
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result
        
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result = []
    
        def helper(node):
            if not node:
                return
            

            helper(node.left)
            result.append(node.val)
            helper(node.right)
        
        helper(root)
        return result