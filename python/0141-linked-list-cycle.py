# [DSA] 141. Linked List Cycle
- **Focus:** Linked Structures (Tier 3)
- **Source:** LeetCode
- **Link:** https://leetcode.com/problems/linked-list-cycle/

## Problem Statement
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

## Approach: Floyd's Tortoise and Hare
Use two pointers, `slow` and `fast`. Move `slow` by one step and `fast` by two steps. If there is a cycle, the two pointers will eventually meet.

```python
# Solution template for projects/leetcodeSols/python/0141-linked-list-cycle.py
```
