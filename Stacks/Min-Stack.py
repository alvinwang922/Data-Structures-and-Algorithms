"""
Design a stack that supports push, pop, top, and retrieving 
the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int):
        self.stack.append(x)

    def pop(self):
        self.stack.pop(len(self.stack) - 1)

    def top(self):
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        return min(self.stack)


"""
Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
"""
