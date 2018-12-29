class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = []
        while n != 1:
            n = sum([pow(int(c), 2) for c in str(n)])
            if n in mem or n == 1:
                break
            else:
                mem.append(n)
        return n == 1
