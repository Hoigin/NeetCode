class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = [[] for _ in range(n)]
        visited = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(i):
            visited.add(i)
            for ne in graph[i]:
                if ne not in visited:
                    dfs(ne)
        
        dfs(0)
        return len(visited)==n