from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        dr = [(-1, 0), (1, 0),(0, 1), (0, -1)]
        @cache
        def dfs(i, j):
            curr = matrix[i][j]
            matrix[i][j] = '*'
            temp = 1
            for di, dj in dr:
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] != '*' and matrix[x][y] > curr:
                    temp = max(temp, dfs(x, y) + 1)
            matrix[i][j] = curr
            return temp
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res