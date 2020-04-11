# Day 10 - Completed 4/11/2020 (early AM)
# Min Stack - 155. Min Stack
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/
# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.minVal = float("inf")


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        if x < self.minVal:
            self.minVal = x

    def updateMin(self):
        tmpStack = []
        newMin = float("inf")
        while len(self.s) > 0:
            item = self.s.pop()
            tmpStack.append(item)
            if item < newMin:
                newMin = item
        while len(tmpStack) > 0:
            self.s.append(tmpStack.pop())
        self.minVal = newMin

    def pop(self):
        """
        :rtype: None
        """
        item = self.s.pop()
        if item == self.minVal:
            self.updateMin()
        return item


    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal

# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 56 ms
# Memory Usage: 17.5 MB
# Your runtime beats 92.08 % of python3 submissions.



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()