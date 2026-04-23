class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res1 = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res1 = max(area, res1)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res1
