# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow, fast, length, prev = head, head, 1, None

        while fast.next:
            length += 1
            fast = fast.next
            if length % 2:
                slow = slow.next

        if not length % 2:
            slow = slow.next

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while length > 1:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
            length -= 2
        return True
