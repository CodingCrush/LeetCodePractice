class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        chain = [1] * n
        chain[0] = chain[1] = 0

        for walk in xrange(2, n):
            if chain[walk]:
                for i in xrange(2, (n - 1) / walk + 1):
                    chain[i * walk] = 0
        return sum(chain)
