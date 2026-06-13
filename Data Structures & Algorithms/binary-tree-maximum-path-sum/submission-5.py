# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        node_sum = {None: 0}
        max_sum = float('-inf')

        while stack:
            node = stack[-1]

            if node.left and node.left not in node_sum:
                stack.append(node.left)
            elif node.right and node.right not in node_sum:
                stack.append(node.right)
            else:
                stack.pop()
                left_sum = node_sum[node.left]
                right_sum = node_sum[node.right]

                max_sum = max(max_sum, node.val + max(0, left_sum) + max(0, right_sum))

                node_sum[node] = node.val + max([0, left_sum, right_sum])

        return max_sum



    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
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