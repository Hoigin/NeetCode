class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num = [[1 if r==0 or c==0 else 0 for c in range(n)] for r in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                num[r][c] = num[r-1][c] + num[r][c-1]
        return num[-1][-1]