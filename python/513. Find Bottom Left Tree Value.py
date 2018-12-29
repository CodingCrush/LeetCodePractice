# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        res = [root]
        bot_lft = None
        while res:
            bot_lft = res[0].val
            res = [p for node in res for p in (node.left, node.right) if p]
        return bot_lft
