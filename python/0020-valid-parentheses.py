class Solution:
    def isValid(self, s: str) -> bool:
        getOpener = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in getOpener:
                if not stack or stack.pop() != getOpener[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack
            