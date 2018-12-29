class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = 0

        if not nums:
            return 0

        for head in range(1, len(nums)):
            if nums[head] != nums[tail]:
                tail += 1
                nums[tail] = nums[head]
        return tail + 1
