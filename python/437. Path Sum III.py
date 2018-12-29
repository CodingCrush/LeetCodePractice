# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        ret = 0
        if not root:
            return 0
        ret += self.dfs(root, sum)
        return ret + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, node, remain):
        match = 0
        if not node:
            return 0
        if remain == node.val:
            match += 1
        match += self.dfs(node.left, remain - node.val)
        match += self.dfs(node.right, remain - node.val)
        return match


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, node, remain):
        if not node:
            return 0
        return self.dfs(node.left, remain - node.val)+self.dfs(node.right, remain - node.val)+(remain == node.val)
