class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = len(s)
        ret = ''
        for i in range(length / k / 2):
            ret = ''.join((ret, s[k * i * 2:k * i * 2 + k][::-1], s[k * i * 2 + k:k * (i + 1) * 2]))

        left = length - length / k / 2 * k * 2
        if length <= k:
            ret = ''.join((ret, s[length - left::][::-1]))
        else:
            ret = ''.join((ret, s[length - left:length - left + k][::-1], s[length - left + k:]))
        return ret
