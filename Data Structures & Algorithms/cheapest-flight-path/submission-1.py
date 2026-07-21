class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        graph = [[] for _ in range(n)]
        for s, d, p in flights:
            graph[s].append((d, p))
        dist = [[INF] * (k+2) for _ in range(n)]
        heap = [(0, src, -1)]
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops == k or cost > dist[node][stops+1]:
                continue
            for next_node, p in graph[node]:
                if cost + p < dist[next_node][stops+2]:
                    dist[next_node][stops+2] = cost + p
                    heapq.heappush(heap, (cost + p, next_node, stops+1))
        return -1