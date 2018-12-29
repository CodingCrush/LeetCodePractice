class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        idx, ret = 1, [1] * length
        while idx < length:
            ret[idx] = ret[idx - 1] * nums[idx - 1]
            idx += 1

        idx -= 2
        count = 1
        while idx >= 0:
            count *= nums[idx + 1]
            ret[idx] = ret[idx] * count
            idx -= 1
        return ret
