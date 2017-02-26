class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) < 2:
            return len(s)
        tmp = ""
        last = None
        for char in s:
            if last == char == " ":
                continue
            tmp += char
            last = char
        return len(tmp.split(' '))
