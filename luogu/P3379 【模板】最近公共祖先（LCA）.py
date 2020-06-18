import sys, heapq
from collections import *


class lca:
    def __init__(self, n, s, g):
        self.g = g
        self.tin = defaultdict(int)
        self.tout = defaultdict(int)
        self.sz = 0
        while n:
            self.sz += 1
            n //= 2
        self.t = 0
        self.arr = defaultdict(list)
        self.dfs(s, s)

    def dfs(self, cur, parent):
        self.t += 1
        self.tin[cur] = self.t
        self.arr[cur] = [parent]*self.sz
        for i in range(1, self.sz):
            self.arr[cur][i] = self.arr[self.arr[cur][i - 1]][i - 1]
        for nxt in self.g[cur]:
            if nxt == parent: continue
            self.dfs(nxt, cur)
        self.tout[cur] = self.t

    def isAncestor(self, u, v):
        return self.tin[u] <= self.tin[v] and self.tout[u] >= self.tout[v]

    def query(self, u, v):
        if self.isAncestor(u, v):
            return u
        if self.isAncestor(v, u):
            return v
        for i in range(self.sz)[::-1]:
            if not self.isAncestor(self.arr[u][i], v):
                u = self.arr[u][i]
        return self.arr[u][0]


def main():
    # sys.stdin = open('input.txt', 'r')
    n, m, s = map(int, input().split(' '))
    g = defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().split(' '))
        g[x].append(y)
        g[y].append(x)
    mylca = lca(n, s, g)
    for _ in range(m):
        u, v = map(int, input().split(' '))
        print(mylca.query(u, v))


if __name__ == "__main__":
    main()


