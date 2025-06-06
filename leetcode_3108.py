class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        # Union by size
        if self.size[xr] < self.size[yr]:
            self.parent[xr] = yr
            self.size[yr] += self.size[xr]
        else:
            self.parent[yr] = xr
            self.size[xr] += self.size[yr]

class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        # 1. Build Components
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v)

        # 2. Get cost of each component
        component_cost = {}  # root -> cost
        for u, v, w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w

        # 3. Queries
        res = []
        for src, dst in query:
            r1, r2 = uf.find(src), uf.find(dst)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(component_cost[r1])
        return res
