class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        for val in (2, 3, 5):
            while num % val == 0:
                num /= val
        return num == 1
