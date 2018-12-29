class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profile, index = 0, 0
        while index < len(prices)-1:
            diff = prices[index+1]-prices[index]
            if diff > 0:
                profile += diff
            index += 1
        return profile
# Using index is faster then iterator.
