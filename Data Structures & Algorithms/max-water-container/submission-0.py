class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_cap = 0
        while left < right:
            curr_cap = min(heights[left],heights[right]) * (right-left)
            if curr_cap > max_cap:
                max_cap = curr_cap
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_cap