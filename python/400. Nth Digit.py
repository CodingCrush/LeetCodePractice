class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, base, step = 1, 1, 9
        while n > base*step:
            n -= base*step
            base += 1
            step *= 10
            start *= 10
        return int(str(start + (n - 1) / base)[(n - 1) % base])
