# Problem: Find the Index of the First Occurrence in a String
# Goal: Master Python string slicing `string[i:i+len]` and `for i in range()` loops.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i
        
        return -1
