class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        def array_search(array, value):
            for _value in array:
                if _value > value:
                    return _value
            return -1

        for index, value in enumerate(findNums):
            index_of_value = nums.index(value)
            findNums[index] = array_search(nums[index_of_value:], value)

        return findNums
