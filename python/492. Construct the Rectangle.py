class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math

        min_l = int(math.sqrt(area))
        for l in xrange(min_l, area + 1):
            if area % l == 0 and l >= (area / l):
                return [l, area / l]
