# import collections
# n, m = list(map(int,input().split()))
# price = list(map(int,input().split()))
# graph = collections.defaultdict(list)
# dp = [[False]*n for _ in range(n)]
# for _ in range(m):
#     a, b, state = list(map(int,input().split()))
#     a -= 1
#     b -= 1
#     if state == 2:
#         graph[b].append(a)
#         dp[b][a] = True
#     graph[a].append(b)
#     dp[a][b] = True

# for _ in range(n):
#     dp2 = dp.copy()
#     for i in range(n):
#         for j in range(n):
#             if not dp2[i][j]:
#                 continue
#             for k in graph[j]:
#                 dp[i][k] = True

# print(max([0]+[price[i]-price[j] for i in range(n) for j in range(n) if dp[0][i] and dp[i][j] and dp[j][n-1]]))

import sys
f = open("input.txt")
sys.stdin = f

class Graph:
    def __init__(self,n):
        self.g = collections.defaultdict(list)
        self.reach = [False]*n
        self.val = [float('inf')]*n

    def add_edge(self,a,b):
        self.g[a].append(b)

    def cover(self,start):
        q = collections.deque([start])
        self.reach[start] = True
        while q:
            cur = q.popleft()
            for nxt in self.g[cur]:
                if not self.reach[nxt]:
                    self.reach[nxt] = True
                    q.append(nxt)

    def bfs(self,start,price_):
        if self.val[start] <= price_:
            return
        q = collections.deque([start])
        self.val[start] = price_
        while q:
            cur = q.popleft()
            for nxt in self.g[cur]:
                if self.val[nxt] > price_:
                    self.val[nxt] = price_
                    q.append(nxt)

import collections
n, m = list(map(int,input().split()))
price = list(map(int,input().split()))
mp, fmp = Graph(n), Graph(n)
for _ in range(m):
    a, b, state = list(map(int,input().split()))
    a -= 1
    b -= 1
    if state == 2:
        mp.add_edge(b,a)
        fmp.add_edge(a,b)
    mp.add_edge(a,b)
    fmp.add_edge(b,a)
mp.cover(0)
fmp.cover(n-1)
# print(mp.g)
# print(fmp.g)
# print(mp.reach)
# print(fmp.reach)
idx = sorted([i for i in range(n)], key = lambda x: price[x])
# print(idx)
for i in idx:
    if mp.reach[i]:
        mp.bfs(i,price[i])
for i in idx[::-1]:
    if fmp.reach[i]:
        fmp.bfs(i,-price[i])

# print(mp.val)
# print(fmp.val)

print(max(-fmp.val[i]-mp.val[i] for i in range(n)))