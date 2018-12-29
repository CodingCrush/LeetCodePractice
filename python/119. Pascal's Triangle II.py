class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        for _ in xrange(0, rowIndex):
            for idx in xrange(len(ret)-1, 0, -1):
                ret[idx] += ret[idx-1]
            ret.append(1)
        return ret
