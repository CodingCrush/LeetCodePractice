# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        head, tail = 1, n
        if isBadVersion(head):
            tail = head

        while tail - head > 1:
            mid = (head + tail) / 2
            if isBadVersion(mid):
                tail = mid
            else:
                head = mid
        return tail
