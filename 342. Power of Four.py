class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        string = bin(num)[2:]
        return string.count('0') == len(string)-1 and string.count('0') % 2 == 0
