# Reference: https://leetcode.com/problems/container-with-most-water/
# Goal: Find two lines that together with the x-axis forms a container, such that the container contains the most water.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = 0

        while left < right:
            area = min(heights[left], heights[right])*(right-left)
            maxArea = max(maxArea, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
            
