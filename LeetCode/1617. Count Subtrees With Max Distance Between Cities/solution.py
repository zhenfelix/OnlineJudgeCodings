# class Solution(object):
#     def countSubgraphsForEachDiameter(self, n, edges):
#         graph = {}
#         for e in edges:
#             f,t = e[0],e[1]
#             if f not in graph:
#                 graph[f] = []
#             graph[f].append(t)
#             if t not in graph:
#                 graph[t] = []
#             graph[t].append(f)
            
#         # check for all combinations
#         ans = [0] * (n-1)
#         for com in range(0,2**n):
#             cg = {}
#             for node in range(0,n):
#                 if com & (1 << node):
#                     node = node+1
#                     if node not in cg:
#                         cg[node] = []
#                     for e in graph[node]:
#                         if 1<<(e-1) & com:
#                             cg[node].append(e)
                            
#             if len(cg.keys()) > 1:
#                 dia = self.find_dia(cg)
#                 # print cg, dia
#                 if dia >= 1:
#                     ans[dia-1] += 1
#         return ans
    
#   # check if connected, and caculate diameter
#     def find_dia(self, graph):
#         start = list(graph.keys())[0]
#         q = [(start,0)]
#         v = {start:True}
#         f_node = start
#         f_len = 0
        
#         while q:
#             cn,cd = q.pop(0)
#             if cd > f_len:
#                 f_len = cd
#                 f_node = cn
#             if cn in graph:
#                 for e in graph[cn]:
#                     if e not in v:
#                         q.append((e,cd+1))
#                         v[e] = True
                        
#         if len(v.keys()) != len(graph.keys()):
#             return 0
#         if f_len < 1:
#             return 1
        
#         start = f_node
#         q = [(start,0)]
#         v = {start:True}
#         dia = 0
        
#         while q:
#             cn,cd = q.pop(0)
#             dia = max(dia, cd)
#             if cn in graph:
#                 for e in graph[cn]:
#                     if e not in v:
#                         q.append((e,cd+1))
#                         v[e] = True
#         return dia

# class Solution:
#     def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
#         res = [0]*(n-1)
#         g = defaultdict(list)
#         cur, nxt = set(), set()
#         for a, b in edges:
#             a -= 1
#             b -= 1
#             g[a].append(b)
#             g[b].append(a)
#         dis = [[0]*n for _ in range(n)]
#         def dfs(root, cur, depth, parent):
#             dis[root][cur] = depth
#             for nxt in g[cur]:
#                 if nxt == parent:
#                     continue
#                 dfs(root, nxt, depth+1, cur)
#             return

#         for i in range(n):
#             dfs(i,i,0,-1)
            
#         # print(dis)

#         def connected(cur):
#             for i in range(n):
#                 if cur & (1<<i):
#                     start = i 
#                     break

#             todo = [cur]        

#             def helper(x):
#                 todo[0] ^= (1<<x)
#                 for y in g[x]:
#                     if todo[0] & (1<<y):
#                         helper(y)
#                 return

#             helper(start)
#             return todo[-1] == 0


#         for state in range(1,1<<(n)):
#             if connected(state):
#                 d = max(dis[i][j] for i in range(n) for j in range(n) if ((1<<i)&state) and ((1<<j)&state))
#                 # print(state,d)
#                 if d  > 0:
#                     res[d-1] += 1
#         return res


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0]*(n-1)
        g = defaultdict(list)
        gs = [0]*n
        dp = [0]*(1<<n)
        for a, b in edges:
            a -= 1
            b -= 1
            g[a].append(b)
            g[b].append(a)
            gs[a] |= (1<<b)
            gs[b] |= (1<<a)
            dp[(1<<a)|(1<<b)] = 1
        dis = [[0]*n for _ in range(n)]
        def dfs(root, cur, depth, parent):
            dis[root][cur] = depth
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                dfs(root, nxt, depth+1, cur)
            return

        for i in range(n):
            dfs(i,i,0,-1)
            
#         print(dis)
#         print(ees)
        
        for state in range(1<<n):
            # print(state, dp[state])
            if dp[state] > 0:
                res[dp[state]-1] += 1
                for i in range(n):
                    if dp[state | (1<<i)] == 0 and (state & gs[i]):
                        dp[state | (1<<i)] = max(dp[state], max(dis[i][j] for j in range(n) if state&(1<<j)))
                    # if dp[state | (1<<i)] == 0 and any((i,j) in ees for j in range(n) if state&(1<<j)):
                    #     dp[state | (1<<i)] = max(dp[state], max(dis[i][j] for j in range(n) if state&(1<<j)))
                    # if state & (1<<i) == 0 and any((i,j) in ees for j in range(n) if state&(1<<j)):
                        # dp[state ^ (1<<i)] = max(dp[state ^ (1<<i)], dp[state], max(dis[i][j] for j in range(n) if state&(1<<j)))
        return res



# class Solution:
#     def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
#         res = [0]*(n-1)
#         g = defaultdict(list)
        
#         for a, b in edges:
#             a -= 1
#             b -= 1
#             g[a].append(b)
#             g[b].append(a)
            
#         def dfs(state, cur, parent):
#             cnt, d1, d2, D = 0, 0, 0, 0
#             for nxt in g[cur]:
#                 if nxt == parent or (state & (1<<nxt) == 0):
#                     continue
#                 cnt_, d_, D_ = dfs(state, nxt, cur)
#                 cnt += cnt_
#                 d_ += 1
#                 D = max(D, D_)
#                 if d_ > d1:
#                     d1, d2 = d_, d1
#                 elif d_ > d2:
#                     d2 = d_
            
#             return cnt+1, d1, max(d1+d2, D)
        
#         for state in range(1,1<<n):
#             start = bin(state)[::-1].find('1')
#             cc, _, dd = dfs(state, start, -1)
#             if dd > 0 and cc == bin(state).count('1'):
#                 res[dd-1] += 1
#         return res
