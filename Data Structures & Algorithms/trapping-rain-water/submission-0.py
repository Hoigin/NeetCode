class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        temp_left, temp_right = 0, 0
        lefts = [0] * n
        rights = [0] * n
        for i in range(n):
            temp_left = max(temp_left, height[i])
            lefts[i] = temp_left
            temp_right = max(temp_right, height[n-i-1])
            rights[n-i-1] = temp_right
        for i in range(1, n-1):
            if lefts[i] <= height[i] or rights[i] <= height[i]:
                continue
            res += (min(lefts[i], rights[i]) - height[i])
        return res