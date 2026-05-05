class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid) , len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
        while queue:
            row ,col = queue.popleft()
            for dr , dc in directions:
                nr , nc = row + dr , col + dc
                if nr < 0 or nr >=ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = 1 + grid[row][col] 
                queue.append((nr,nc))