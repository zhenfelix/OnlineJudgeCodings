class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(y)] = find(x)

        n = len(edges)
        parent = [0 for i in range(n+1)]
        first, second = None, None
        for e in edges:
            if parent[e[1]] == 0:
                parent[e[1]] = e[0]
            else:
                first = [parent[e[1]], e[1]]
                second = e.copy()
        print(first,second)
        for i in range(1,n+1):
            parent[i] = i 
        for e in edges:
            if e == second:
                continue
            print(e)
            if find(e[0]) == find(e[1]):
                if first:
                    return first
                else:
                    return e
            union(e[0], e[1])
        return second