# from collections import defaultdict

# class Solution:
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
#         visited = [None]*n
#         reach = [None]*n
#         g = defaultdict(list)
#         for e in connections:
#             g[e[0]].append(e[1])
#             g[e[1]].append(e[0])
        
#         def dfs(cur, depth, pre):
#             visited[cur] = depth
#             reach[cur] = depth 
#             for nxt in g[cur]:
#                 if visited[nxt] == None:
#                     dfs(nxt, depth+1, cur)
#                     reach[cur] = min(reach[cur], reach[nxt])
#                 elif nxt != pre:
#                     reach[cur] = min(reach[cur], visited[nxt])
#             if pre != None and visited[cur] == reach[cur]:
#                 res.append([pre,cur])
#             return
        
#         res = []
#         dfs(0, 0, None)
    
#         return res

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        low = [-1]*n

        def dfs(parent,cur,level):
            low[cur] = level
            for nxt in g[cur]:
                if parent == nxt:
                    continue
                if low[nxt] == -1:
                    dfs(cur,nxt,level+1)
                low[cur] = min(low[cur],low[nxt])
                if low[nxt] > level:
                    res.append([cur,nxt])
        
        res = []
        dfs(-1,0,0)
        # print(low)
        return res
