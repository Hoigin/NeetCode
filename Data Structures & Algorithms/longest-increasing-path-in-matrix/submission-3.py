class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        dr = [(-1, 0), (1, 0),(0, 1), (0, -1)]
        dp = {}
        def dfs(i, j, preVal):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= preVal:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            temp = 1
            temp = max(temp, dfs(i+1, j, matrix[i][j]) + 1)
            temp = max(temp, dfs(i-1, j, matrix[i][j]) + 1)
            temp = max(temp, dfs(i, j+1, matrix[i][j]) + 1)
            temp = max(temp, dfs(i, j-1, matrix[i][j]) + 1)
            dp[(i, j)] = temp
            return temp
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, -1))
        return res    