class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        repo = {}
        for idx, num in enumerate(nums):
            if repo.get(target-num, -1) == -1:
                repo[num] = idx
            else:
                return [idx, repo[target-num]]
