class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        group = []
        for c in s:
            if c in group:
                continue
            else:
                group.append(c)
            if s.count(c) == 1:
                return s.index(c)
        return -1


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        repo = {}
        for c in s:
            try:
                repo[c] += 1
            except KeyError:
                repo[c] = 1
        if 1 not in repo.values():
            return -1
        for index, c in enumerate(s):
            if repo[c] == 1:
                return index
