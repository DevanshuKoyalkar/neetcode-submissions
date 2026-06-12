# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        stack = [(root, root.val)]
        good_node_count = 0

        while stack: # process parent and then children
            node, max_val_seen = stack.pop()

            if node.val >= max_val_seen:
                good_node_count += 1
            
            child_max_val_seen = max(max_val_seen, node.val)
            
            if node.right:
                stack.append((node.right, child_max_val_seen))
            if node.left:
                stack.append((node.left, child_max_val_seen))
            
        return good_node_count

    def goodNodes2(self, root: TreeNode) -> int:
        good_node_count = 0

        def dfs(node, max_val):
            nonlocal good_node_count
            if not node:
                return
            
            if node.val >= max_val:
                good_node_count += 1
            
            child_max_val = max(max_val, node.val)
            dfs(node.left, child_max_val)
            dfs(node.right, child_max_val)
        
        dfs(root, -10000)
        return good_node_count
