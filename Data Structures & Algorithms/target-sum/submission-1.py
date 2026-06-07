class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def backtrack(i, current_sum):
            if i == n:
                return 1 if current_sum == target else 0
            if (i, current_sum) in dp:
                return dp[(i, current_sum)]
            dp[(i, current_sum)] = backtrack(i+1, current_sum+nums[i]) + backtrack(i+1, current_sum-nums[i])
            return dp[(i, current_sum)]
        return backtrack(0, 0)