# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [root]
        visited = set()
        postorder = []
        while stack:
            node = stack[-1]

            # post order traversal 
            if node.left and node.left not in visited:
                stack.append(node.left)
            elif node.right and node.right not in visited:
                stack.append(node.right)
            else:
                stack.pop()
                visited.add(node)
                postorder.append(node.val)

        return postorder

    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def helper(node):
            if not node:
                return
            
            helper(node.left)
            helper(node.right)

            result.append(node.val)
        
        helper(root)
        return result