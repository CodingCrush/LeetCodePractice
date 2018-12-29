class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self._deq = deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self._deq.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self._deq.popleft()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self._deq[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self._deq) == 0

        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()
