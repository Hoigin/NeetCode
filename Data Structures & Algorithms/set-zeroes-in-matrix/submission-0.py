class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_pos = set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_pos.add((r, c))
        for r, c in zero_pos:
            matrix[r] = [0] * n
            for i in range(m):
                matrix[i][c] = 0