class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def isSurrounded(r, c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if board[r][c] == 'O':
                board[r][c] = '#'
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r+dr, c+dc
                    isSurrounded(nr, nc)
        
        for i in range(rows):
            isSurrounded(i, 0)
        for i in range(rows):
            isSurrounded(i, cols-1)
        for i in range(cols):
            isSurrounded(0, i)
        for i in range(cols):
            isSurrounded(rows-1, i)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'