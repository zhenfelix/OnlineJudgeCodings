import sys, heapq
from collections import *
from functools import cmp_to_key

def dfs(cur):
    visited.add(cur)
    pid, cursz, curscnt, curarea = cur, 1, scnt[cur], area[cur]
    for nxt in g[cur]:
        if nxt in visited: continue
        nxtid, nxtsz, nxtscnt, nxtarea = dfs(nxt)
        cursz += nxtsz
        curscnt += nxtscnt
        curarea += nxtarea
        pid = min(pid, nxtid)
    return pid, cursz, curscnt, curarea

# sys.stdin = open('input.txt', 'r')
n = int(input())
persons = set()
g = defaultdict(set)
scnt, area = defaultdict(int), defaultdict(int)
visited = set()
for _ in range(n):
    arr = input().split(' ')
    pid = arr[0]
    persons |= set([pid])
    k = int(arr[3])
    nxtids = arr[1:3]+arr[4:4+k]
    for nxt in nxtids:
        if nxt == '-1': continue
        g[pid].add(nxt)
        g[nxt].add(pid)
        persons |= set([nxt])
    scnt[pid], area[pid] = int(arr[-2]), int(arr[-1])

res = []
for person in persons:
    if person in visited:
        continue
    res.append(dfs(person))

res.sort(key=lambda x: (-x[-1]/x[1],x[0]))
print(len(res))
for pid, cursz, curscnt, curarea in res:
    print("{} {} {:.3f} {:.3f}".format(pid,cursz,curscnt/cursz,curarea/cursz))