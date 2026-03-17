# Solution Template: 0020-valid-parentheses.py

# Problem: Valid Parentheses
# URL: https://neetcode.io/problems/validate-parentheses
# Category: DSA (Stack)
# Status: Pending

def isValid(s: str) -> bool:
    # TODO: Implement using a stack
    pass

if __name__ == "__main__":
    # Test cases
    print(isValid("()"))      # Expected: True
    print(isValid("()[]{}"))  # Expected: True
    print(isValid("(]"))      # Expected: False
    print(isValid("([)]"))    # Expected: False
    print(isValid("{[]}"))     # Expected: True
