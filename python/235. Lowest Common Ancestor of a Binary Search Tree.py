# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node:
                return
            if min(p.val, q.val) > node.val:
                return dfs(node.right)
            elif max(p.val, q.val) < node.val:
                return dfs(node.left)
            else:
                return node
        return dfs(root)
