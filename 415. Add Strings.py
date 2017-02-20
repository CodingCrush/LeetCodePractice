class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def cal_int(nums):
            count = 0
            for index, char in enumerate(nums[::-1]):
                count += (ord(char)-ord('0'))*(10**index)
            return count
        return str(cal_int(num1)+cal_int(num2))
