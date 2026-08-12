from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        @cache
        def dfs(i, j):
            if j == n:
                return i == m
            curr = i < m and (s[i] == p[j] or p[j] == '.')
            if j+1 < n and p[j+1] == '*':
                ans = dfs(i, j+2) or (curr and dfs(i+1, j))
            else:
                ans = curr and dfs(i+1, j+1)
            return ans
        return dfs(0, 0)