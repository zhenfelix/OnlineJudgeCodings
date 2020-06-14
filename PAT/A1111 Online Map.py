import sys, heapq
from collections import *
from functools import cmp_to_key



# sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split(' '))
gd = defaultdict(list)
gt = defaultdict(list)
for _ in range(m):
    v1, v2, oneway, dd, tt = map(int, input().split(' '))
    gd[v1].append((v2,dd,tt))
    gt[v1].append((v2,tt,1))
    if oneway == 1: continue
    gd[v2].append((v1,dd,tt))
    gt[v2].append((v1,tt,1))

source, destination = map(int,input().split(' '))

# def bfs(g):
#     pre = [-1]*n
#     dist = [(float('inf'),float('inf'))]*n
#     q = [((0,0),source)]
#     dist[source] = (0,0)
#     while q:
#         cost, cur = heapq.heappop(q)
#         if cost > dist[cur]: continue
#         if cur == destination: break
#         for nxt,d1,d2 in g[cur]:
#             if (cost[0]+d1,cost[1]+d2) < dist[nxt]:
#                 dist[nxt] = (cost[0]+d1,cost[1]+d2)
#                 heapq.heappush(q,((cost[0]+d1,cost[1]+d2),nxt))
#                 pre[nxt] = cur
#     path, cur = [], destination
#     while cur != -1:
#         path.append(cur)
#         cur = pre[cur]
#     return path[::-1], dist[destination]

def bfs(g):
    pre = [-1]*n
    dist = [(float('inf'),float('inf'))]*n
    visited = set()
    dist[source] = (0,0)
    for _ in range(n):
        cost, cur = (float('inf'),float('inf')), -1
        for i in range(n):
            if i in visited: continue
            if dist[i] < cost:
                cost = dist[i]
                cur = i
        visited.add(cur)
        if cur == destination: break
        for nxt,d1,d2 in g[cur]:
            if nxt in visited: continue
            if (cost[0]+d1,cost[1]+d2) < dist[nxt]:
                dist[nxt] = (cost[0]+d1,cost[1]+d2)
                pre[nxt] = cur
    path, cur = [], destination
    while cur != -1:
        path.append(cur)
        cur = pre[cur]
    return path[::-1], dist[destination]

path1, cost1 = bfs(gd)
path2, cost2 = bfs(gt)
if path1 == path2:
    print("Distance = {}; Time = {}: ".format(cost1[0],cost1[1])+" -> ".join(map(str, path1)))
else:
    print("Distance = {}: ".format(cost1[0])+" -> ".join(map(str, path1)))
    print("Time = {}: ".format(cost2[0]) + " -> ".join(map(str, path2)))