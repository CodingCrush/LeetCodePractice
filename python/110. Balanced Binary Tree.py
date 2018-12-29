# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return 0
            return 1 + max(dfs(root.left), dfs(root.right))

        if not root:
            return True
        ans = abs(dfs(root.left) - dfs(root.right)) < 2
        return ans and self.isBalanced(root.left) and self.isBalanced(root.right)
