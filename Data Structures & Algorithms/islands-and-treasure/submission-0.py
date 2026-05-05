class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure_pos = []
        pos = []
        rows = len(grid)
        cols = len(grid[0])
        search_dir = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    treasure_pos.append((i,j))
        for i, j in treasure_pos:
            for x, y in search_dir:
                pos.append((i+x,j+y))

        def bfs(pos, distance):
            new_pos = []
            for i, j in pos:
                if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==-1 or grid[i][j]==0:
                    continue
                if grid[i][j] == 2147483647:
                    grid[i][j] = distance
                    for x, y in search_dir:
                        new_pos.append((i+x,j+y))
            if new_pos:
                bfs(new_pos, distance+1)
            else:
                return
        
        bfs(pos, 1)
        return
                