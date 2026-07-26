class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        for i in range(n):
            l = r = i
            while l > 0 and heights[l-1] >= heights[i]:
                l -= 1
            while r < n-1 and heights[r+1] >= heights[i]:
                r += 1
            maxArea = max(maxArea, heights[i]*(r-l+1))
        return maxArea
