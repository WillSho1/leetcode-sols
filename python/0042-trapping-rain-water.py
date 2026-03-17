# 0042-trapping-rain-water.py
# Goal: Compute how much water can be trapped after raining.
# Reference: https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height)-1
        maxLeft = height[left]
        maxRight = height[right]

        # keep gap for water
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]

        return water