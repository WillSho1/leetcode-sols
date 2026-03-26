# Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Goal: Find the length of the longest substring without repeating characters in O(N).

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = set()
        left = 0
        right = 0
        maxString = 0

        while right < len(s):
            while s[right] in subSet:
                subSet.remove(s[left])
                left += 1
            subSet.add(s[right])
            maxString = max(maxString, len(subSet))
            right += 1
        
        return maxString
