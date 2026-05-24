# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
        


    def lowestCommonAncestor1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
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


        ptr1, ptr2 = 0, 0
        result = ptr1

        while ptr1 < len(path_p) and ptr2 < len(path_q) and path_p[ptr1].val == path_q[ptr2].val:
            result = path_p[ptr1]
            ptr1 += 1
            ptr2 += 1

        return result
