# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def combine_vals(root):
            if not root:
                return " "
            else:
                return str(root.val)+str(combine_vals(root.left))+str(combine_vals(root.right))

        return combine_vals(p) == combine_vals(q)
