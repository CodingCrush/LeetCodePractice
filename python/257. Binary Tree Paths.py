# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        ret = []

        def dfs(root, string):
            if not root.left and not root.right:
                ret.append((string + "->" + str(root.val))[2:])
            if root.left:
                dfs(root.left, string + "->" + str(root.val))
            if root.right:
                dfs(root.right, string + "->" + str(root.val))
        dfs(root, "")
        return ret
