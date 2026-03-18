# Solution Template: 0020-valid-parentheses.py

# Problem: Valid Parentheses
# URL: https://neetcode.io/problems/validate-parentheses
# Category: DSA (Stack)
# Status: Pending

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}': '{', ']': '[', ')': '('}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif not stack or stack.pop() != mapping[char]:
                return False

        return not stack
