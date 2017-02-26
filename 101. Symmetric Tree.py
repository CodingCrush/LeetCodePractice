# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Breath-first-serch
        layout = [root]
        while layout:
            tmp = []
            for node in layout:
                if node:
                    tmp.append(node.val)
                else:
                    tmp.append(None)
            if tmp != tmp[::-1]:
                return False
            # Remove useless None node
            layout = [node for node in layout if node]
            layout = [p for node in layout for p in (node.left, node.right)]
        return True
