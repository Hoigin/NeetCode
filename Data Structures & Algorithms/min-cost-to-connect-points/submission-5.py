class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        par = list(range(n))
        def find(node):
            while node != par[node]:
                node = par[node]
            return node
        def union(node_i, node_j):
            par_i, par_j = find(node_i), find(node_j)
            if par_i == par_j:
                return False
            par[par_i] = par_j
            return True
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                edges.append((cost, i, j))
        edges.sort()
        res = 0
        count = 0
        for cost, i , j in edges:
            if union(i, j):
                count += 1
                res += cost
                if count == n-1:
                    break
        return res
        