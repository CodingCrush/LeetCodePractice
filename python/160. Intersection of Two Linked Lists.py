# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB:
            return None

        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        lengthA, lengthB = get_length(headA), get_length(headB)

        while lengthA != lengthB:
            if lengthA > lengthB:
                headA = headA.next
                lengthA -= 1
            else:
                headB = headB.next
                lengthB -= 1

        while headA:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next
        return None
