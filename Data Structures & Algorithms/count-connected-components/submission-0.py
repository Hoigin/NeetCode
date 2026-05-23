class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = [False] * n

        def dfs(i):
            visit[i] = True
            for ne in graph[i]:
                if not visit[ne]:
                    dfs(ne)
        
        for i in range(n):
            if not visit[i]:
                dfs(i)
                res += 1
        return res