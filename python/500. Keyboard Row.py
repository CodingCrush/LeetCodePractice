class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        tmp = []
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset('qwertyuiop') or word_set.issubset('asdfghjkl') or word_set.issubset('zxcvbnm'):
                tmp.append(word)
        return tmp