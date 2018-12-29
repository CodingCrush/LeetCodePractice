class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(nums) - min(nums) * len(nums)


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        moves = 0
        min_value = min(nums)
        for value in nums:
            moves += (value-min_value)
        return moves
