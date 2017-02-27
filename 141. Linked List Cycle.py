# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        cursor = head.next
        count = 0
        while cursor:
            count += 1
            if head.val == cursor.val:
                return True
            cursor=cursor.next
            if count == 2:
                head = head.next
                count = 0
        return False
