import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():
    def dfs(cur,visited,dist,cntb,cntc):
        nonlocal res
        if cur == n:
            if cntb == cntc: res = min(res,dist)
            return
        for nxt, aa, bb, cc in g[cur]:
            if nxt in visited: continue
            dfs(nxt,visited|set([nxt]),dist+aa,cntb,cntc)
            dfs(nxt,visited|set([nxt]),dist+bb,cntb+1,cntc)
            dfs(nxt,visited|set([nxt]),dist+cc,cntb,cntc+1)
        return



    # sys.stdin = open('input.txt', 'r')
    n, m = map(int, input().split(' '))
    g = defaultdict(list)
    res = float('inf')
    for _ in range(m):
        u, v, a, b, c = map(int, input().split(' '))
        g[u].append((v,a,b,c))
        g[v].append((u,a,b,c))
    dfs(1,set(),0,0,0)
    print(res)






if __name__ == "__main__":
    main()


