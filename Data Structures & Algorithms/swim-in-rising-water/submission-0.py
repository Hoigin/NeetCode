import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n-1 and c == n-1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_t = max(t, grid[nr][nc])
                    heapq.heappush(heap, (new_t, nr, nc))
        return -1