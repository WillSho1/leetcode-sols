#!/usr/bin/env python3
"""
LeetCode 0003: Longest Substring Without Repeating Characters
Category: DSA/Sliding Window
Difficulty: Medium

Problem: Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    max_len = 0
    start = 0
    
    for end in range(len(s)):
        if s[end] in char_map:
            # Move start to the right of the previous occurrence
            start = max(start, char_map[s[end]] + 1)
        
        char_map[s[end]] = end
        max_len = max(max_len, end - start + 1)
        
    return max_len

if __name__ == "__main__":
    # Test cases
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    print("All test cases passed.")
