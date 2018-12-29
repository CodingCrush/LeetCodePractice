class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        assemble = "".join(S.split("-")).upper()
        ret = []
        index = len(assemble)
        while index > K:
            ret.append(assemble[index - K:index])
            index -= K
        ret.append(assemble[:index])
        return "-".join(ret[::-1])
