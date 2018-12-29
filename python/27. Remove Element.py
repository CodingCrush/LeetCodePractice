class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        head = 0

        while head < len(nums):
            try:
                while nums[-1] == val:
                    nums.pop()
            except IndexError:
                break
            if nums[head] == val:
                nums[-1], nums[head] = nums[head], nums[-1]
            else:
                head += 1
        return len(nums)
