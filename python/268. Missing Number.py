class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num, min_num = nums[0], nums[0]
        total = 0
        for num in nums:
            if num > max_num:
                max_num = num
            elif num < min_num:
                min_num = num
            total += num
        diff = max_num * (max_num + 1) / 2 - total
        if min_num > 0:
            return 0
        elif diff == 0:
            return max_num + 1
        else:
            return diff
