class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        for u in graph:
            graph[u].sort(reverse=True)
        print(graph)
        res = []
        def dfs(curr):
            while graph[curr]:
                nxt = graph[curr].pop()
                dfs(nxt)
            res.append(curr)
        dfs("JFK")
        return res[::-1]
