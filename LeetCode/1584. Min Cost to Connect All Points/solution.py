class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(n):
                if i == j: continue
                edges.append((dist(points[i],points[j]),i,j))

        heapq.heapify(edges)
        sums, cnt = 0, 0
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
                return 1
            return 0
        while cnt < n-1:
            cost, a, b = heapq.heappop(edges)
            tmp = union(a,b)
            if tmp == 1:
                cnt += 1
                sums += cost
        return sums

