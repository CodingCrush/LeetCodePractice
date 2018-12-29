class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        origin = set(range(1, len(nums)+1))
        sub = set(nums)
        return list(origin-sub)
