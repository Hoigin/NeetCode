class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        def dfs(node, parent):
            if visited[node]:
                return True
            visited[node] = True
            for ne in adj[node]:
                if ne == parent:
                    continue
                if dfs(ne, node):
                    return True
            return False
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visited = [False] * (n+1)
            if dfs(a, -1):
                return [a, b]
        return []