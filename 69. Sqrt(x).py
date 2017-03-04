class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 1, x
        if x < 2:
            return x

        while end - start > 1:
            mid = (start + end) / 2
            if mid ** 2 > x:
                end = mid
            else:
                start = mid
        return start
