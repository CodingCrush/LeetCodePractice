class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import OrderedDict
        res1, res2=OrderedDict(), OrderedDict()
        for idx in xrange(0, len(s)):
            res1[s[idx]] = res1.get(s[idx], 0)+idx
            res2[t[idx]] = res2.get(t[idx], 0)+idx

        return res1.values() == res2.values()
