class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [['*'] * (n+1) for _ in range(m+1)]
        def dfs(i, j):
            if dp[i][j] != '*':
                return dp[i][j]
            if j == n:
                return i == m
            curr = i < m and (s[i] == p[j] or p[j] == '.')
            if j+1 < n and p[j+1] == '*':
                ans = dfs(i, j+2) or (curr and dfs(i+1, j))
            else:
                ans = curr and dfs(i+1, j+1)
            dp[i][j] = ans
            return ans
        return dfs(0, 0)