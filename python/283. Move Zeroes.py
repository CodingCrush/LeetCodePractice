class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zero_count = 0
        for index in xrange(length):
            if nums[index] == 0:
                zero_count += 1
                continue
            else:
                nums[index-zero_count] = nums[index]
        while zero_count:
            nums[-zero_count] = 0
            zero_count -= 1
