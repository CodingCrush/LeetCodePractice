# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = head
        while head and head.next:
            if head.next.val == head.val:
                if head.next.next:
                    useless = head.next
                    head.next = head.next.next
                    useless.next = None
                else:
                    useless = head.next
                    head.next = None
                    useless.next = None
            else:
                head = head.next
        return ret
