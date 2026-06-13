# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # max sum till root 
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            node_sum = node.val + max(0, left_sum) + max(0, right_sum)

            # print(node.val, node_sum)
            max_sum = max(max_sum, node_sum)
            return node.val + max([0,left_sum, right_sum])
        
        dfs(root)
        return max_sum