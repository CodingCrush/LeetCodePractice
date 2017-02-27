# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        def dfs(root, remain):
            if not root:
                if remain == 0:
                    return True
                return False
            if root.left and root.right:
                return dfs(root.left, remain - root.val) or dfs(root.right, remain - root.val)
            elif root.left:
                return dfs(root.left, remain - root.val)
            else:
                return dfs(root.right, remain - root.val)
        return dfs(root, sum)
