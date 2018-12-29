# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret, depth_nodes = [], [root]
        while depth_nodes:
            ret.append([node.val for node in depth_nodes])

            depth_nodes = [p for node in depth_nodes for p in (node.left, node.right) if p]
        ret.reverse()
        return ret
