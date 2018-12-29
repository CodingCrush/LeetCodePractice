class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        couple = {"{": "}", "(": ")", "[": "]"}
        stash = []
        for char in s:
            if char in "({[":
                stash.append(char)
            else:
                if not stash or couple[stash.pop()] != char:
                    return False
        return not stash
