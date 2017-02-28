# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth, layer = 0, [root]

        while layer:
            depth += 1

            for node in layer:
                if not node:
                    return depth
                if not node.left and not node.right:
                    return depth
            layer = [p for node in layer for p in (node.left, node.right) if p]
        return depth
