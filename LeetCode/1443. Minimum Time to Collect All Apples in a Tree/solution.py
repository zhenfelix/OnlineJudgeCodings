class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        ans = 0
        def dfs(root, parent):
            nonlocal ans
            has_apple = hasApple[root]
            for child in g[root]:
                if child != parent:
                    tmp = dfs(child, root)
                    has_apple = has_apple or tmp
            if has_apple and root != 0:
                ans += 1
            return has_apple
        
        dfs(0, -1)
        return ans * 2


# class Solution:
#     def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
#         graph = defaultdict(list)
#         for a, b in edges:
#             graph[a].append(b)
#             graph[b].append(a)
#         sums = [0]*n
#         def cnt(cur, pre):
#             sums[cur] += hasApple[cur]
#             for nxt in graph[cur]:
#                 if nxt == pre:
#                     continue
#                 sums[cur] += cnt(nxt, cur)
#             return sums[cur]

#         def dfs(cur, pre):
#             dis = 0
#             if sums[cur] == 0:
#                 return dis
#             for nxt in graph[cur]:
#                 if nxt == pre:
#                     continue
#                 dis += dfs(nxt, cur) + 2*(sums[nxt] != 0)
#             return dis

#         cnt(0,-1)
#         return dfs(0,-1)
