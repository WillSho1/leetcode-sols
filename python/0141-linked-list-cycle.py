# Problem: Linked List Cycle
# Goal: Master the "Floyd's Tortoise and Hare" (Fast/Slow Pointer) algorithm.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head

        while hare != None and hare.next != None:
            turtle = turtle.next
            hare = hare.next.next

            if turtle == hare:
                return True
        
        return False