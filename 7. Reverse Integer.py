class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = int(str(x)[::-1])
            return x if x <= (2**31-1) else 0
        else:
            x = int("".join(("-", str(abs(x))[::-1])))
            return x if x >= (-2**31) else 0
