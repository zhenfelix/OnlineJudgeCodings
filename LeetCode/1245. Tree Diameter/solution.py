# class Solution:
#     def treeDiameter(self, edges: List[List[int]]) -> int:
#         g = collections.defaultdict(list)
#         for a, b in edges:
#             g[a].append(b)
#             g[b].append(a)

#         def dfs(cur, visited):
#             h1, h2 = 0, 0
#             for nxt in g[cur]:
#                 if nxt not in visited:
#                     visited.add(nxt)
#                     h = dfs(nxt, visited)+1
#                     visited.remove(nxt)
#                     if h > h1:
#                         h1, h2 = h, h1
#                     elif h > h2:
#                         h2 = h
#             res[0] = max(res[0], h1+h2)
#             return h1

#         res = [0]
#         covered = set()
#         covered.add(0)
#         dfs(0,covered)
#         return res[0]

# class Solution:
#     def treeDiameter(self, edges: List[List[int]], move: int = 0) -> int:
#         graph = collections.defaultdict(set)
#         for a, b in edges:
#             graph[a].add(b)
#             graph[b].add(a)
#         bfs = {(u, None) for u, nex in graph.items() if len(nex) == 1}
#         while bfs:
#             bfs, move = {(v, u) for u, pre in bfs for v in graph[u] if v != pre}, move + 1
#         return max(move - 1, 0)


# class Solution:
#     diameter = 0
#     def treeDiameter(self, edges: List[List[int]], move: int = 0) -> int:
#         def dfs(node, pre):
#             d1 = d2 = 0
#             for nex in graph[node]:
#                 if nex != pre:
#                     d = dfs(nex, node)
#                     if d > d1:
#                         d1, d2 = d, d1
#                     elif d > d2:
#                         d2 = d
#             self.diameter = max(self.diameter, d1 + d2)
#             return d1 + 1
#         graph = collections.defaultdict(set)
#         for a, b in edges:
#             graph[a].add(b)
#             graph[b].add(a)
#         dfs(0, None)
#         return self.diameter

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def bfs(start):
            endpoint, level = 0, 0
            # q = collections.deque([(start, None)])
            q = [(start, None)]
            while q:
                # n = len(q)
                # for _ in range(n):
                #     cur, parent = q.popleft()
                #     endpoint = cur
                #     for x in g[cur]:
                #         if x != parent:
                #             q.append((x,cur))

                q, endpoint, level = [(x,cur) for cur, parent in q for x in g[cur] if x != parent], q[0][0], level+1
            return endpoint, level

        endpoint_, _ = bfs(0)
        _, res = bfs(endpoint_)
        return res-1