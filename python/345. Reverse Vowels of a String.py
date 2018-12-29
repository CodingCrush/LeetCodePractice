class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        head, tail = 0, len(s) - 1
        s = list(s)

        while True:
            if s[head] not in vowels:
                head += 1
            if s[tail] not in vowels:
                tail -= 1
            if head >= tail:
                break

            if s[head] in vowels and s[tail] in vowels:
                s[head], s[tail] = s[tail], s[head]
                head += 1
                tail -= 1

        return "".join(s)
