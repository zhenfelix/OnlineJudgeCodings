# class Solution:
#     def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         m = len(queries)
#         edgeList.append([-1,-1,float('inf')])
#         edgeList.sort(key=lambda x: x[-1])
#         idx = sorted([i for i in range(m)], key=lambda x: queries[x][-1])
#         res = [False]*m
#         parent = [i for i in range(n)]
#         def find(cur):
#             if parent[cur] != cur:
#                 parent[cur] = find(parent[cur])
#             return parent[cur]
#         def union(a,b):
#             ra, rb = find(a), find(b)
#             if ra != rb:
#                 parent[ra] = rb
#                 return False
#             return True
#         pos = 0
#         for u, v, e in edgeList:
#             while pos < m and queries[idx[pos]][-1] <= e:
#                 p, q, _ = queries[idx[pos]]
#                 if find(p) == find(q):
#                     res[idx[pos]] = True
#                 pos += 1

#             if u >= 0 and v >= 0:
#                 union(u,v)
#         return res 
                


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        m = len(queries)
        # edgeList.append([-1,-1,float('inf')])
        edgeList.sort(key=lambda x: x[-1])
        idx = sorted([i for i in range(m)], key=lambda x: queries[x][-1])
        res = [False]*m
        parent = [i for i in range(n)]
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                return False
            return True
        pos = 0
        for i in range(m):
            p, q, limit = queries[idx[i]]
            while pos < len(edgeList) and edgeList[pos][-1] < limit:
                u, v, _ = edgeList[pos]
                union(u,v)
                pos += 1

            if find(p) == find(q):
                res[idx[i]] = True
                
        return res 
                

