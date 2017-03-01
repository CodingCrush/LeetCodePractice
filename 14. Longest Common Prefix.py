class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count = 0
        if not strs:
            return ""
        while True:
            try:
                length = len(set(map(lambda strs: strs[count], strs)))
            except IndexError:
                return strs[0][:count]
            if length == 1:
                count += 1
            else:
                return strs[0][:count]
