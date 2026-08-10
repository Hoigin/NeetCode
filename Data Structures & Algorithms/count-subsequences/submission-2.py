class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [['*']*n for _ in range(m)]
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            if dp[i][j] != '*':
                return dp[i][j]
            res = dfs(i+1, j)
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            dp[i][j] = res
            return res
        return dfs(0, 0) 