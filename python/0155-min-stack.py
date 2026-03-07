# LeetCode 155: Min Stack
# Category: Stack & Queue (DSA Tier 2)
# Difficulty: Medium

"""
Problem: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Methods:
- push(val) -- Push element val onto stack.
- pop() -- Removes the element on the top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack:
    def __init__(self):
        # We use two stacks:
        # 1. main_stack - to store all elements
        # 2. min_stack  - to store the minimum value at each point in time
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        # If min_stack is empty or val is <= current min, push to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.main_stack:
            return
        
        removed_val = self.main_stack.pop()
        # If the removed value is the current minimum, pop from min_stack too
        if removed_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Complexity Analysis:
# Time: O(1) for all operations (push, pop, top, getMin)
# Space: O(N) where N is the number of elements pushed onto the stack.
