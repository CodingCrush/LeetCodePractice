class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        head, tail = 0, num
        while tail-head > 1:
            mid = (head+tail)/2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                tail = mid
            else:
                head = mid
        if tail**2 == num:
            return True
        return False
