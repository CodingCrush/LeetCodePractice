class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.deq = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.deq.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.deq.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.deq[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.deq)

