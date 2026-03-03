from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        turtle = head
        hare = head
        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
        
        mid = turtle.next
        turtle.next = None
        prev = None
        
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        

        first = head
        mid = prev

        while mid:
            temp1 = first.next
            temp2 = mid.next

            first.next = mid
            mid.next = temp1

            first = temp1
            mid = temp2