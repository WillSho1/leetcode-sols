from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        height_left = height[start]
        height_right = height[end]

        rain = 0

        while start < end:
            if height_left < height_right:
                start += 1
                height_left = max(height_left, height[start])
                rain += height_left - height[start]
            else:
                end -= 1
                height_right = max(height_right, height[end])
                rain += height_right - height[end]

        return rain