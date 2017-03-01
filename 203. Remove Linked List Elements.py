# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cursor = head

        prev = None
        while cursor:
            if cursor.val == val:
                if prev:
                    prev.next = cursor.next
                    cursor = prev.next
                else:
                    cursor = head = head.next
                continue
            else:
                prev = cursor

            if not cursor:
                break
            cursor = cursor.next
        return head
