class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        repo = {}
        for c in magazine:
            try:
                repo[c] += 1
            except KeyError:
                repo[c] = 1
        for c in ransomNote:
            try:
                repo[c] -= 1
            except KeyError:
                return False
        if repo == {}:
            return True
        if min(repo.values()) < 0:
            return False
        return True


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True
