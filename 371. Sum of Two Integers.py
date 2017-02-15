class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int

        s = a
        carry = b
        while carry:
            t = s ^ carry
            carry = (s & carry) << 1
            s = t
        return s
        """
        return int.__add__(a, b)
