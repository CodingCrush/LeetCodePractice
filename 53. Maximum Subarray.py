class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp, ret, max_val = 0, 0, nums[0]
        for val in nums:
            tmp += val
            if tmp > ret:
                ret = tmp
            elif tmp < 0:
                tmp = 0
            if val > max_val:
                max_val = val

        if max_val < 0:
            return max_val
        return ret
