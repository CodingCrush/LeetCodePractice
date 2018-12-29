class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        head = 1
        while head < len(s):
            if s[head] == s[0] and len(s) % head == 0:
                satisfy = True
                for i in range(1, len(s) / head):
                    if s[:head] != s[head * i:head * (i + 1)]:
                        satisfy = False
                if satisfy:
                    return True
            head += 1
        return False
