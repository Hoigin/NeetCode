from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dfs(i, s):
            if i < n:
                return dfs(i+1, s+nums[i]) + dfs(i+1, s-nums[i])
            else:
                if s == target:
                    return 1
                else:
                    return 0
        return dfs(0, 0)