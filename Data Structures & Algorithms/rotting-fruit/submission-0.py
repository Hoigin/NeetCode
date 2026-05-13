class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = set()
        rotten = deque()
        minutes = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
        while fresh and rotten:
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + dx, j + dy
                    if 0<= x < rows and 0<= y < cols and grid[x][y] == 1:
                        fresh.remove((x, y)) 
                        grid[x][y] = 2
                        rotten.append((x, y))
            minutes += 1
        return -1 if fresh else minutes