# EK with matrix implementation

import sys, heapq
from collections import *

sys.setrecursionlimit(10 ** 6)


class solve:
    def __init__(self, g, s, t):
        self.n = len(g)
        self.g = g
        self.s = s
        self.t = t

    def EK(self):
        res = 0
        while True:
            delta = self.bfs()
            if delta == 0:
                break
            res += delta
        return res

    def bfs(self):
        pre = [-1] * self.n
        flow = [-1] * self.n
        pre[self.s] = self.s
        flow[self.s] = float('inf')
        q = deque()
        q.append(self.s)
        while q:
            cur = q.popleft()
            if cur == self.t:
                break
            for nxt in range(self.n):
                if self.g[cur][nxt] and pre[nxt] == -1:
                    pre[nxt] = cur
                    flow[nxt] = min(flow[cur], self.g[cur][nxt])
                    q.append(nxt)
        if pre[self.t] == -1:
            return 0
        cur = self.t
        while cur != self.s:
            last = pre[cur]
            self.g[last][cur] -= flow[self.t]
            self.g[cur][last] += flow[self.t]
            cur = last
        return flow[self.t]


def main():
    sys.stdin = open('input.txt', 'r')
    n, m, s, t = map(int, input().strip().split(' '))
    g = [[0] * n for _ in range(n)]
    for _ in range(m):
        x, y, w = map(int, input().strip().split(' '))
        g[x - 1][y - 1] = w
    mysolve = solve(g, s-1, t-1)
    print(mysolve.EK())


if __name__ == "__main__":
    main()


# EK with adj linked list implementation

import sys, heapq
from collections import *

sys.setrecursionlimit(10 ** 6)


class solve:
    def __init__(self, n, edges, g, s, t):
        self.n = n
        self.edges = edges
        self.g = g
        self.s = s
        self.t = t

    def EK(self):
        res = 0
        while True:
            delta = self.bfs()
            if delta == 0:
                break
            res += delta
        return res

    def bfs(self):
        pre = [-1] * self.n
        flow = [-1] * self.n
        pre[self.s] = None
        flow[self.s] = float('inf')
        q = deque()
        q.append(self.s)
        while q:
            cur = q.popleft()
            if cur == self.t:
                break
            for idx in self.g[cur]:
                u, v, w = self.edges[idx]
                if w > 0 and pre[v] == -1:
                    pre[v] = idx
                    flow[v] = min(flow[cur], w)
                    q.append(v)
        if pre[self.t] == -1:
            return 0
        cur = self.t
        while cur != self.s:
            last = pre[cur]
            self.edges[last][-1] -= flow[self.t]
            self.edges[last^1][-1] += flow[self.t]
            cur = self.edges[last][0]
        return flow[self.t]


def main():
    # sys.stdin = open('input.txt', 'r')
    n, m, s, t = map(int, input().strip().split(' '))
    edges = [[-1,-1,0] for _ in range(2*m)]
    g = defaultdict(list)
    for i in range(m):
        x, y, w = map(int, input().strip().split(' '))
        edges[i*2] = [x-1,y-1,w]
        g[x-1].append(i*2)
        edges[i*2+1] = [y-1,x-1,0]
        g[y-1].append(i*2+1)
    mysolve = solve(n, edges, g, s-1, t-1)
    print(mysolve.EK())


if __name__ == "__main__":
    main()


# Dinic implementation

import sys, heapq
from collections import *

sys.setrecursionlimit(10 ** 6)


class solve:
    def __init__(self, n, edges, g, s, t):
        self.n = n
        self.edges = edges
        self.g = g
        self.s = s
        self.t = t

    def Dinic(self):
        res = 0
        while self.bfs():
            res += self.dfs(self.s, float('inf'))
        return res

    def bfs(self):
        self.level = [-1]*self.n
        self.ptr = [0]*self.n
        q = deque()
        q.append(self.s)
        self.level[self.s] = 0
        while q:
            cur = q.popleft()
            for idx in self.g[cur]:
                _, nxt, w = self.edges[idx]
                if w > 0 and self.level[nxt] == -1:
                    self.level[nxt] = self.level[cur] + 1
                    q.append(nxt)
        return self.level[self.t] != -1

    def dfs(self, cur, limit):
        if cur == self.t:
            return limit
        res = 0
        i = self.ptr[cur]
        while i < len(self.g[cur]):
            self.ptr[cur] = i
            idx = self.g[cur][i]
            _, nxt, w = self.edges[idx]
            if w > 0 and self.level[nxt] == self.level[cur]+1:
                tmp = self.dfs(nxt,min(w,limit))
                res += tmp
                limit -= tmp
                self.edges[idx][-1] -= tmp
                self.edges[idx^1][-1] += tmp
                if limit == 0:
                    return res
            i += 1
        return res






def main():
    # sys.stdin = open('input.txt', 'r')
    n, m, s, t = map(int, input().strip().split(' '))
    edges = [[-1,-1,0] for _ in range(2*m)]
    g = defaultdict(list)
    for i in range(m):
        x, y, w = map(int, input().strip().split(' '))
        edges[i*2] = [x-1,y-1,w]
        g[x-1].append(i*2)
        edges[i*2+1] = [y-1,x-1,0]
        g[y-1].append(i*2+1)
    mysolve = solve(n, edges, g, s-1, t-1)
    print(mysolve.Dinic())


if __name__ == "__main__":
    main()


