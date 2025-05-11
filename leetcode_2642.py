import heapq

class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.adj = {i: [] for i in range(n)}
        for u, v, w in edges:
            self.adj[u].append((v, w))

    def addEdge(self, edge: list[int]) -> None:
        u, v, w = edge
        self.adj[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = {i: float('inf') for i in range(self.n)}
        dist[node1] = 0
        pq = [(0, node1)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            if u == node2:
                return d

            for v, w in self.adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return -1