class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        while head:
            next = head.next
            head.next = previous
            previous = head
            head = next
        return previous
