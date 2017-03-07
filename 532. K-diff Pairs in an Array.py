class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        seen = set()
        from bisect import bisect_left

        length = len(nums)
        for at, val in enumerate(nums):
            idx = bisect_left(nums, val + k)
            if idx < at:
                continue
            if k == 0:
                idx += 1
            if idx >= length:
                break
            if nums[idx] == val + k and not (val, val + k) in seen:
                seen.add((val, val + k))
        return len(seen)
