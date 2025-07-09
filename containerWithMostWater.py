from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_a = 0

        start = 0
        end = len(height)-1

        while start != end:
            area = (end - start)*min(height[start], height[end])
            max_a = max(max_a, area)

            if height[start] < height[end]:
                start += 1
            else:
                end -=1

        return max_a