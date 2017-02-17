class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        g_index = s_index = 0

        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                g_index += 1
            s_index += 1
        return g_index
