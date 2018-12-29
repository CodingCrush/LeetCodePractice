class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def memo(f):
            class memodict(dict):
                def __init__(self, f):
                    self.f = f

                def __call__(self, *args):
                    return self[args]

                def __missing__(self, key):
                    ret = self[key] = self.f(*key)
                    return ret
            return memodict(f)

        @memo
        def solve(remain):
            if remain == 1:
                return 1
            if remain == 2:
                return 2
            return solve(remain - 1) + solve(remain - 2)
        return solve(n)
