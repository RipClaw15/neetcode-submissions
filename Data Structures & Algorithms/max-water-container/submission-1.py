class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1
        max_t = 0
        while l < r :
            t = (r - l) * min(heights[l],heights[r])
            if t > max_t:
                max_t = t
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1
        return max_t