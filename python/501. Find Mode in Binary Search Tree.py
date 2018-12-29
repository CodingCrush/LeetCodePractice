# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import Counter
        rst = Counter()

        def dfs(node):
            if not node:
                return
            rst[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        try:
            max_count_value = max(rst.values())
            return [key for key, value in rst.items() if value == max_count_value]
        except ValueError:
            return []
