# Problem: Valid Anagram
# Goal: Master frequency counting with dictionaries or sorting.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        countDict = {}

        for char in s:
            countDict[char] = countDict.get(char, 0)+1
        
        for char in t:
            if char not in countDict or countDict[char] == 0:
                return False
            countDict[char] -= 1
        
        return True
        