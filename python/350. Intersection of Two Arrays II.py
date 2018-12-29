class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        ret = []
        tail1, tail2 = len(nums1)-1, len(nums2)-1
        while tail1 >= 0 and tail2 >= 0:
            if nums1[tail1] == nums2[tail2]:
                ret.append(nums1[tail1])
                tail1 -= 1
                tail2 -= 1
            elif nums1[tail1] > nums2[tail2]:
                tail1 -= 1
            else:
                tail2 -= 1
        return ret
