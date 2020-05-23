import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():

    def dfs(cur,parent,d):
        if cur in people:
            return d, cur
        res = [(float('inf'),float('inf'))]
        for nxt in g[cur]:
            if nxt == parent: continue
            nxtd, nxtcur = dfs(nxt,cur,d+1)
            res.append((nxtd,nxtcur))
        return min(res)



    # sys.stdin = open('input.txt', 'r')
    # print(input().split(' '))
    n, m = map(int, input().split(' '))
    g = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split(' '))
        g[a].append(b)
        g[b].append(a)

    people = set(list(map(int,input().split(' '))))
    # print(g)
    # print(people)
    print(dfs(1,0,0)[-1])






if __name__ == "__main__":
    main()


