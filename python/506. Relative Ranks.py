class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sor_nums = sorted(nums)
        tmp = {}
        try:
            if len(tmp) == 0:
                tmp[sor_nums.pop()] = "Gold Medal"
            if len(tmp) == 1:
                tmp[sor_nums.pop()] = "Silver Medal"
            if len(tmp) == 2:
                tmp[sor_nums.pop()] = "Bronze Medal"
        except IndexError:
            pass
        while sor_nums:
            tmp[sor_nums.pop()] = str(len(tmp) + 1)
        return [tmp[num] for num in nums]
