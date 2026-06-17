# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # post order traversal and recursive deletion
        if not root:
            return root

        visited = set()
        deleted = set([None])

        stack = [root]

        while stack:
            node = stack[-1]

            if node.left and node.left not in visited:
                stack.append(node.left)
            elif node.right and node.right not in visited:
                stack.append(node.right)
            else:
                stack.pop()
                visited.add(node)

                if node.left in deleted and node.right in deleted and node.val == target:
                    deleted.add(node)
                
                if node.left in deleted:
                    node.left = None
                if node.right in deleted:
                    node.right = None
        
        if root in deleted:
            return None
        
        return root
