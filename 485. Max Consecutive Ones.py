class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = []
        for value in nums:
            if value:
                if not count:
                    count.append(1)
                else:
                    count[-1] += 1
            else:
                count.append(0)
        return max(count)
