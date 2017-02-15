class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dd = {}
        for value in nums:
            dd[value] = dd.get(value, 0) + 1
        for key, count in dd.items():
            if count == 1:
                return key


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for value in nums:
            ret ^= value
        return ret
