class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = []
        is_minus = False
        if num < 0:
            is_minus = True
        num = abs(num)
        while num >= 7:
            ret.append(str(num % 7))
            num = int(num/float(7))
        ret.append(str(num))
        if is_minus:
            ret.append("-")
        return "".join(ret[::-1])
