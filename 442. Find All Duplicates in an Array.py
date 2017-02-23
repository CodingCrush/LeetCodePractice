class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for val in nums:
            if nums[abs(val)-1] < 0:
                ret.append(abs(val))
            nums[abs(val) - 1] *= -1
        return ret
