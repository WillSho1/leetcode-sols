class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        stack = []
        mapping = {'{':'}', '[':']', '(':')'}

        for char in s:
            if char in mapping:
                stack.append(mapping[char])
            elif char in mapping.values():
                if not stack or char != stack.pop():
                    return False

        return not stack