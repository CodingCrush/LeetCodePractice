class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        from bisect import bisect
        heaters.sort()
        relaxation = 0

        for house in houses:
            position = bisect(heaters, house)
            if position == 0:
                lft = float('inf')
            else:
                lft = house - heaters[position - 1]
            if position == len(heaters):
                rgt = float('inf')
            else:
                rgt = heaters[position] - house
            relaxation = max(relaxation, min(lft, rgt))
        return relaxation
