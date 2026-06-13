# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        new_node = TreeNode(val)
        if not curr:
            return new_node

        while True:
            if curr.val < val:
                if curr.right: 
                    curr = curr.right
                else:
                    print("inserted, right" + str(curr.val))
                    curr.right = new_node
                    return root
            else:
                if curr.left:
                    curr = curr.left
                else:
                    print("inserted, left " + str(curr.val))
                    curr.left = new_node
                    return root

        return root
        