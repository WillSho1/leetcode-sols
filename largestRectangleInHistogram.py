from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights.append(0)
        stack = [-1]

        for i in range(len(heights)):
            # if height is the rightmost barrier
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                # leftmost barrier is index next in stack
                width = i - stack[-1] - 1
                max_area = max(max_area, height*width)
            stack.append(i)
        
        return max_area