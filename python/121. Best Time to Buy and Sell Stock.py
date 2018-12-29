class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price, profile = prices[0], 0
        for price in prices:
            min_price = min(min_price, price)
            profile = max(profile, price - min_price)
        return profile
