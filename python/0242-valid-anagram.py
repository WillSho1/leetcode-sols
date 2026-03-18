# Problem: Valid Anagram
# Goal: Master frequency counting with dictionaries or sorting.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freqDict = {}

        for char in s:
            freqDict[char] = freqDict.get(char, 0) + 1

        for char in t:
            if char not in freqDict or freqDict[char] == 0:
                return False
            freqDict[char] -= 1

        return True
        