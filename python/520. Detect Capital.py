class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.title() == word:
            return True
        if word.lower() == word:
            return True
        if word.upper() == word:
            return True
        return False
