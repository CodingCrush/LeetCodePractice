class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        pair, single = 0, 0
        for value in [s.count(c) for c in set(s)]:
            if value == 1:
                single += 1
            elif value%2 == 0:
                pair += value
            else:
                pair += value-1
                single += 1
        return pair+1 if single else pair
