class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        left = 0
        global_max = 0

        for right in range(len(s)):
            while s[right] and s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            global_max = max(global_max, len(letters))
        
        return global_max