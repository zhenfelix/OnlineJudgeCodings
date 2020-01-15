class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(cur):
            if parent[cur] == cur:
                return cur
            parent[cur] = find(parent[cur])
            return parent[cur]
        
        def union(x, y):
            
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
                
        if len(connections) < n-1:
            return -1
        parent = [i for i in range(n)]
        # print(parent)
        for a, b in connections:
            # print(a,b)
            union(a,b)
        # print(parent)
        return len(set([find(i) for i in range(n)])) - 1



# class Solution:
#     def makeConnected(self, n, connections):
#         if len(connections) < n - 1: return -1
#         G = [set() for i in range(n)]
#         for i, j in connections:
#             G[i].add(j)
#             G[j].add(i)
#         seen = [0] * n

#         def dfs(i):
#             if seen[i]: return 0
#             seen[i] = 1
#             for j in G[i]: dfs(j)
#             return 1

#         return sum(dfs(i) for i in range(n)) - 1