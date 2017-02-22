class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        match = ['0', '1', '2', '3',
                 '4', '5', '6', '7',
                 '8', '9', 'a', 'b',
                 'c', 'd', 'e', 'f']
        ret = ""
        if num < 0:
            num += 2**32
        if num == 0:
            return '0'
        while num:
            num, remainder = divmod(num, 16)
            ret = "".join((match[remainder], ret))
        return ret
