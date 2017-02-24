class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = "".join(str(n) for n in digits)
        digits = str(int(digits)+1)
        return [int(i) for i in digits]
