# Day 10 - Completed 4/11/2020 (early AM)
# Difficulty - Easy
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
        self.stack = []
        self.min = None #idx of min val

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append(x)
            if self.stack[self.min] > x:
                self.min = len(self.stack) - 1
        else:
            self.min = 0
            self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop(-1)
        if self.stack == []:
            self.min = None
        elif self.min == len(self.stack):
            self.min = self.stack.index(min(self.stack))
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min == None:
            return None
        else:
            return self.stack[self.min] 

# Submission Detail
# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 17.5 MB
# Your runtime beats 81.88 % of python3 submissions.

# Works but not very efficient
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> None:
        self.stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        
# Submission Detail
# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 856 ms
# Memory Usage: 17.6 MB
# Your runtime beats 7.86 % of python3 submissions.
'''        
#####
# Prev Submission - slow
'''
class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class MinStack:

    def __init__(self, head= None):
        """
        initialize your data structure here.
        """
        self.head = head

    def push(self, x: int) -> None:
        x = Element(x)
        if self.head == None:
            self.head = x
        else:
            x.next = self.head
            self.head = x           

    def pop(self) -> None:
        self.head = self.head.next
        

    def top(self) -> int:
        return self.head.value
        

    def getMin(self) -> int:
        current = self.head
        min_val = current.value
        while True:
            if current.value < min_val:
                min_val = current.value
            if current.next:
                current = current.next
            else:
                break
        return min_val
'''
# Submission Detail
# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 7208 ms
# Memory Usage: 18.6 MB

# Runtime is very very slow because of the min function checking the whole linked list.


# old solution from online
'''
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
'''

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# New Solution after learning data structures - Doesn't work, not sure why
'''
class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class MinStack:

    def __init__(self, head= None):
        """
        initialize your data structure here.
        """
        self.head = head
        self.min = None

    def push(self, x: int) -> None:
        x = Element(x)
        if self.head == None:
            self.head = x
            self.min = self.head
        else:
            x.next = self.head
            self.head = x
            if self.head.value < self.min.value:
                self.min = self.head

    def pop(self) -> None:
        if self.min == self.head and self.head.next:
            self.head = self.head.next
            self.update_min()
        elif self.min == self.head and self.head.next == None:
            self.head = self.head.next
            self.min = None
        else:
            self.head = self.head.next

    def update_min(self):
        current = self.head
        min_obj = current
        min_val = current.value
        while True:
            if current.value < min_val:
                min_obj = current
            if current.next:
                current = current.next
            else:
                break
        self.min = min_obj

    def top(self) -> int:
        return self.head.value
        

    def getMin(self) -> int:
        return self.min.value
'''