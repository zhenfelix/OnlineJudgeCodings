class Solution:
    def minimumCost(self, N: int, conections: List[List[int]]) -> int:
        parent = {}
        for i in range(1,N+1,1):
            parent[i] = i
            
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        conections = sorted(conections, key = lambda x:x[2])
        costs, cc = 0, 0
        for c in conections:
            u, v, cost = c[0], c[1], c[2]
            parent[u], parent[v] = find(u), find(v)
            if parent[u] != parent[v]:
                parent[parent[v]] = parent[u]
                cc += 1
                costs += cost
            if cc == N-1:
                break
        if cc < N-1:
            return -1
        return costs
        