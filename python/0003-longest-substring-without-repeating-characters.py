# Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Goal: Find the length of the longest substring without repeating characters in O(N).

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        substringSet = set()

        head = 0
        tail = 0

        while head < len(s):
            if s[head] not in substringSet:
                substringSet.add(s[head])
                maxLength = max(maxLength, head+1-tail)
                head += 1
            else:
                substringSet.remove(s[tail])
                tail += 1

        return maxLength

