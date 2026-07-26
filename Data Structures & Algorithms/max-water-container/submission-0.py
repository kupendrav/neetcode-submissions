from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        
        while left < right:
            # Calculate area
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            max_area = max(max_area, area)
            
            # Move the pointer of the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
