class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n > 26:
            t = n % 26
            if t:
                res.append(t)
                n /= 26
            else:
                res.append(26)
                n = (n - 26) / 26
        res.append(n)
        return "".join([chr(ord('A') + val - 1) for val in res[::-1]])
