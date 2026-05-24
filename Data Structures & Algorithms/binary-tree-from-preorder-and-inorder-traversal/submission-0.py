# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        LEN = len(preorder)

        def helper(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_start > preorder_end:
                return None
             
            root = TreeNode(preorder[preorder_start])

            if preorder_start == preorder_end:
                return root

            for pos in range(inorder_start, inorder_end + 1):
                if inorder[pos] == root.val:
                    left_nodes = pos - inorder_start
                    right_nodes = inorder_end - pos

                    left_preorder_start = preorder_start + 1
                    left_preorder_end = left_preorder_start + left_nodes - 1

                    right_preorder_start = left_preorder_end + 1
                    right_preorder_end = preorder_end

                    left_inorder_start = inorder_start
                    left_inorder_end = pos - 1
                    right_inorder_start = pos + 1
                    right_inorder_end = inorder_end

                    break
            
            root.left = helper(
                left_preorder_start,
                left_preorder_end,
                left_inorder_start,
                left_inorder_end
            )
            root.right = helper(
                right_preorder_start,
                right_preorder_end,
                right_inorder_start,
                right_inorder_end
            )

            return root

        return helper(0, LEN - 1, 0, LEN - 1)
                
            

