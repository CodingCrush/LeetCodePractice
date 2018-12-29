class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        head, tail = 1, n
        while (tail - head) > 1:
            mid = (head+tail)/2
            if mid*(mid+1)/2 > n:
                tail = mid
            else:
                head = mid
        return head
