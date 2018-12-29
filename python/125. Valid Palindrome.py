class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        allowed = 'abcdefghijklmnopqrstuvwxyz'
        allowed += 'ABCEDFGHIJKLMNOPQRSTUVWXYZ'
        allowed += '0123456789'
        head, tail = 0, len(s)-1
        while tail > head:
            if not s[tail] in allowed:
                tail -= 1
            elif not s[head] in allowed:
                head += 1
            elif s[head] in allowed and s[tail] in allowed:
                if s[head].lower() != s[tail].lower():
                    return False
                head += 1
                tail -= 1
        return True
