class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        count = 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        layers = 0
        while count < m*n:
            for j in range(layers, n-layers):
                if count == m*n:
                    break
                res.append(matrix[layers][j])
                count += 1
            for i in range(layers+1, m-layers):
                if count == m*n:
                    break
                res.append(matrix[i][n-layers-1])
                count += 1
            for j in range(n-layers-2, layers-1, -1):
                if count == m*n:
                    break
                res.append(matrix[m-layers-1][j])
                count += 1
            for i in range(m-layers-2, layers, -1):
                if count == m*n:
                    break
                res.append(matrix[i][layers])
                count += 1
            layers += 1
        return res