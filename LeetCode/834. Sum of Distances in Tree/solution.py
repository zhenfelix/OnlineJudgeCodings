class Solution:
#     def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
#         neibors = collections.defaultdict(list)
#         for a, b in edges:
#             neibors[a].append(b)
#             neibors[b].append(a)
#         parent = [-1]*N 
#         sums = [0]*N 
#         cnts = [1]*N

#         def dfs(cur, p):
#             parent[cur] = p 
#             for nxt in neibors[cur]:
#                 if nxt != p:
#                     dis, cnt = dfs(nxt, cur)
#                     cnts[cur] += cnt 
#                     sums[cur] += cnt + dis 
#             return sums[cur], cnts[cur]

#         dfs(0,-1)
#         # res = [sums[i] for i in range(N)]
#         # def go_up(cur, pre, step):
#         #     if cur == -1:
#         #         return 0
#         #     return sums[cur]-sums[pre]-cnts[pre]+(cnts[cur]-cnts[pre])*step + go_up(parent[cur],cur,step+1)

#         # for i in range(N):
#         #     res[i] += go_up(parent[i],i,1)
#         # return res

#         res = [0]*N
#         def go_down(cur, res_up):
#             p = parent[cur]
#             res[cur] = res_up-sums[cur]-cnts[cur]+N-cnts[cur]+sums[cur]
#             for nxt in neibors[cur]:
#                 if nxt != p:
#                     go_down(nxt, res[cur])
#         # go_down(0,sums[0]+cnts[0])
#         go_down(0,0)
#         return res 


    def sumOfDistancesInTree(self, N, edges):
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return res




