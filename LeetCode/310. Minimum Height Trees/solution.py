# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         nxt = [set() for _ in range(n)]
#         h = [[(0,-1),(0,-1)] for _ in range(n)]
#         for a, b in edges:
#             nxt[a].add(b)
#             nxt[b].add(a)
#         def dfs(cur,pre):
#             for child in nxt[cur]:
#                 if pre != child:
#                     d = dfs(child, cur) + 1
#                     if d > h[cur][0][0]:
#                         h[cur][0], h[cur][1] = (d,child), h[cur][0]
#                     elif d > h[cur][1][0]:
#                         h[cur][1] = (d,child) 
#             return h[cur][0][0]
#         dfs(0,-1)
#         # print(h)
#         res, height = [[]], [float("inf")]
#         def dfs2(cur,pre):
#             if h[cur][0][0] < height[0]:
#                 height[0], res[0] = h[cur][0][0], [cur]
#             elif h[cur][0][0] == height[0]:
#                 res[0].append(cur)

#             for child in nxt[cur]:
#                 if pre != child:
#                     ph = h[cur][0][0]
#                     if child == h[cur][0][-1]:
#                         ph = h[cur][1][0]
#                     if ph+1 >= h[child][0][0]:
#                         h[child][0], h[child][1] = (ph+1,cur), h[child][0]
#                     elif ph+1 >= h[child][1][0]:
#                         h[child][1] = (ph+1,cur)
#                     dfs2(child,cur)
#             return 
#         dfs2(0,-1)
#         # print(h)
#         return res[0]



class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        nxt = [set() for _ in range(n)]
        for a, b in edges:
            nxt[a].add(b)
            nxt[b].add(a)
        q = [x for x in range(n) if len(nxt[x]) == 1]
        res = []
        # print(nxt,q)
        while q:
            res, q = q, []
            for cur in res:
                # print(cur,nxt)
                if not nxt[cur]:
                    continue
                child = nxt[cur].pop()
                nxt[child].remove(cur)
                if len(nxt[child]) == 1:
                    q.append(child)
                                        
        return res


        



