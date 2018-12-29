class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for index, c in enumerate(s):
            count += (ord(c)-ord('A')+1)*(26**(len(s)-index-1))
        return count
