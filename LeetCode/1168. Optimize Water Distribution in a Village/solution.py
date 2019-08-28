class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y) 
            return
        
        edges = []
        for pipe in pipes:
            edges.append(pipe)
        for idx, well in enumerate(wells):
            edges.append([0,idx+1,well])
        # print(edges)
        edges = sorted(edges, key=lambda x: x[2])
        # print(edges)
        parent = [i for i in range(n+1)]
        ans, cc = 0, 0
        for e in edges:
            if find(e[0]) != find(e[1]):
                ans += e[2]
                union(e[0], e[1])
                cc += 1
                if cc == n:
                    break
        return ans
            
        