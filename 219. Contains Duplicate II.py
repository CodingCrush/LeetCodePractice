class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cache = {}
        for idx, val in enumerate(nums):
            if val in cache:
                if idx - cache[val] <= k:
                    return True
            cache[val] = idx
        return False
