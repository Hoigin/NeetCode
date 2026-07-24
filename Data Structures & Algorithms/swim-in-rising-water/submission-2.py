class DSU:
    def __init__(self, n):
        self.par = list(range(n+1))
        self.size = [1] * (n+1)
    def find(self, i):
        if i != self.par[i]:
            i = self.find(self.par[i])
        return i
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return False
        if self.size[pi] < self.size[pj]:
            pi, pj = pj, pi
        self.size[pi] += self.size[pj]
        self.par[pj] = pi
        return True
    def connected(self, i, j):
        return self.find(i) == self.find(j)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n*n)
        altitudes = [(grid[r][c], r, c) for r in range(n) for c in range(n)]
        altitudes.sort()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for t, r, c in altitudes:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] < t:
                    dsu.union(r*n+c, nr*n+nc)
            if dsu. connected(0, n*n-1):
                return t