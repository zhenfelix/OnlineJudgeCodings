# class Solution:
#     def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
#         for i, e in enumerate(edges):
#             edges[i].append(i)
#         edges.sort(key=lambda x:x[-2])
        
#         # print(edges)
#         parent = [i for i in range(n)]
#         def find(cur):
#             if cur == parent[cur]:
#                 return cur 
#             return find(parent[cur])

#         A, B = set([i for i in range(len(edges))]), set()
#         res = []
#         def dfs(idx, st):
#             nonlocal A,B
#             # print(res,st)
#             if res and edges[st[-1]][-2] > edges[res[-1][len(st)-1]][-2]:
#                 return 
#             if len(st) == n-1:
#                 res.append(st)
#                 st = set(st)
#                 A &= st 
#                 B |= st 
#                 # print(st,minsums)
#                 # print(A,B)
#                 return 
#             cur = float(inf)
#             while idx < len(edges):
#                 a, b, w, _ = edges[idx]
#                 ra, rb = find(a), find(b)
#                 if ra != rb and w <= cur:
#                     cur = w 
#                     parent[ra] = rb
#                     dfs(idx+1, st+[idx])
#                     parent[ra] = ra 
#                 idx += 1
#             return True
#         dfs(0,[])
#         # print(mp)
#         # print(A,B)
        
#         return [list(map(lambda x: edges[x][-1],list(A))),list(map(lambda x: edges[x][-1],list(B-A)))]




class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def find(cur):
            if cur != parent[cur]:
                parent[cur] = find(parent[cur])
            return parent[cur]

        def union(a,b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb 
                return True
            return False

        def MST(jump, total):
            sums, cnt = 0, 0
            for i in range(len(edges)):
                if i in jump: continue
                a, b, w, _ = edges[i]
                f = union(a,b)
                cnt += f
                sums += f*w 
                if cnt == total: break
            return sums if cnt == total else float('inf')

        edges = [edge+[i] for i, edge in enumerate(edges)]
        # print(edges)
        edges.sort(key=lambda x: x[-2])
        parent = [i for i in range(n)]
        target = MST([],n-1)
        # print(target)
        A, B = [], []
        for i in range(len(edges)):
            u,v,w,pos = edges[i]
            parent = [i for i in range(n)]
            cur = MST([i],n-1)
            # print(cur)
            if cur > target:
                A.append(pos)
            else:
                parent = [i for i in range(n)]
                union(u,v)
                cur = MST([i],n-2)
                if cur+w == target:
                    B.append(pos)
        return [A,B]
























