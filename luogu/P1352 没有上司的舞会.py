import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():
    def dfs(cur,parent,occupy):
        if occupy:
            return sum([dfs(nxt,cur,False) for nxt in g[cur] if nxt != parent], 0)+arr[cur]
        else:
            return sum([max(dfs(nxt,cur,True),dfs(nxt,cur,False)) for nxt in g[cur] if nxt != parent], 0)


    # sys.stdin = open('input.txt', 'r')
    n = int(input())
    arr = [0]
    g = defaultdict(list)
    children = set()
    for i in range(n):
        arr.append(int(input()))
    for i in range(n-1):
        a, b = map(int,input().split(' '))
        # g[a].append(b)
        g[b].append(a)
        children.add(a)
    root = set(range(1,n+1))-children
    root = root.pop()
    g[0].append(root)
    print(dfs(0,-1,False))





if __name__ == "__main__":
    main()


