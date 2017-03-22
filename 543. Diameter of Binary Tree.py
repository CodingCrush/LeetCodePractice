# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo, self.diameter = {}, 0

        def dfs(root):
            if not root:
                return 0
            lft, rgt = dfs(root.left), dfs(root.right)
            self.diameter = max(self.diameter, lft + rgt)
            memo[root] = 1 + max(lft, rgt)
            return memo[root]

        dfs(root)
        return self.diameter
