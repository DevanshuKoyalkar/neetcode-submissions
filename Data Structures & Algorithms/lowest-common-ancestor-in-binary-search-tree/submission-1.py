# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getPath(target, path):
            curr = root

            while curr:
                path.append(curr)
                if curr.val == target.val:
                    return
                if curr.val > target.val:
                    curr = curr.left
                else:
                    curr = curr.right

        path_p, path_q = [], []

        getPath(p, path_p)
        getPath(q, path_q)

        # print(len(path_p), len(path_q))
        # for node in path_p:
        #     print(node.val, end=" ")
        # print()
        # for node in path_q:
        #     print(node.val, end=" ")
        # print()

        ptr1, ptr2 = 0, 0
        result = ptr1

        while ptr1 < len(path_p) and ptr2 < len(path_q) and path_p[ptr1].val == path_q[ptr2].val:
            result = path_p[ptr1]
            ptr1 += 1
            ptr2 += 1

        return result
