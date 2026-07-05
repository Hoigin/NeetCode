class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if dp[i]:
                end = min(n, i+nums[i]+1)
                for j in range(i+1, end):
                    dp[j] = True
        return dp[-1]