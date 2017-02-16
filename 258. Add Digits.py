class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = 0
        while num > 0:
            tmp += num % 10
            num = int(num / 10)
        if tmp > 9:
            tmp = self.addDigits(tmp)
        return tmp
