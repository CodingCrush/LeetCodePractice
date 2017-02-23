class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import deque
        repo = deque()
        length = 1
        repo.append(nums[0])
        for val in nums[1:]:
            if length == 1:
                if val > repo[-1]:
                    repo.append(val)
                    length += 1
                elif val < repo[0]:
                    repo.appendleft(val)
                    length += 1
            elif length == 2:
                if val > repo[-1]:
                    repo.append(val)
                    length += 1
                elif val < repo[0]:
                    repo.appendleft(val)
                    length += 1
                elif repo[0] < val < repo[1]:
                    repo.append(val)
                    repo[2], repo[1] = repo[1], repo[2]
                    length += 1
            else:
                if val > repo[-1]:
                    repo.popleft()
                    repo.append(val)
                elif repo[1] < val < repo[2]:
                    repo[1], repo[0] = val, repo[1]
                elif repo[0] < val < repo[1]:
                    repo[0] = val
        return repo[0] if length == 3 else repo[-1]
