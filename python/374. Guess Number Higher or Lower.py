# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        head, tail = 1, n
        while tail-head > 1:
            mid = (head+tail)/2
            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                head = mid
            else:
                tail = mid
        if guess(head) == 0:
            return head
        else:
            return tail
