class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import defaultdict
        origin, walk = defaultdict(int), defaultdict(int)
        for key in p:
            origin[key] += 1
        p_length = len(p)
        res = []
        for key in s[:p_length]:
            walk[key] += 1
        if walk == origin:
            res.append(0)
        for idx in xrange(p_length, len(s)):
            remove = s[idx - p_length]
            if walk[remove] == 1:
                del walk[remove]
            else:
                walk[remove] -= 1
            walk[s[idx]] += 1
            if walk == origin:
                res.append(idx - p_length + 1)
        return res
