class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        row = [1]
        for _ in xrange(0, numRows):
            ret.append(row[:])
            row.append(1)
            for i in xrange(len(row) - 2, 0, -1):
                row[i] += row[i - 1]
        return ret
