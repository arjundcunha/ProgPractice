class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minElement = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minElement.append(x)
        self.minElement.sort()
        self.stack = [x] + self.stack

    def pop(self):
        """
        :rtype: void
        """
        self.minElement.remove(self.stack[0])
        self.stack = self.stack[1:]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minElement[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()