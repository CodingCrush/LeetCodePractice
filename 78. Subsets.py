class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for num in nums:
            for t in ret[:]:
                tmp = t[:]
                tmp.append(num)
                ret.append(tmp)
        return ret
