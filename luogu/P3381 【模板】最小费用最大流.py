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

    def MCMF(self):
        flow, cost = 0, 0
        while self.spfa():
            cur = self.t
            while cur != self.s:
                idx = self.pre[cur]
                self.edges[idx][-2] -= self.flow[self.t]
                self.edges[idx ^ 1][-2] += self.flow[self.t]
                cur = self.edges[idx][0]
            flow += self.flow[self.t]
            cost += self.flow[self.t] * self.dis[self.t]
        return flow, cost

    def spfa(self):
        self.pre = [-1] * self.n
        self.flow = [float('inf')] * self.n
        self.dis = [float('inf')] * self.n
        self.vis = [False] * self.n
        q = deque()
        q.append(self.s)
        self.dis[self.s] = 0
        self.vis[self.s] = True
        while q:
            cur = q.popleft()
            self.vis[cur] = False
            for idx in self.g[cur]:
                _, nxt, w, cost = self.edges[idx]
                if w > 0 and self.dis[nxt] > self.dis[cur] + cost:
                    self.flow[nxt] = min(self.flow[cur], w)
                    self.dis[nxt] = self.dis[cur] + cost
                    self.pre[nxt] = idx
                    if not self.vis[nxt]:
                        self.vis[nxt] = True
                        q.append(nxt)
        return self.dis[self.t] < float('inf')


def main():
    # sys.stdin = open('input.txt', 'r')
    n, m, s, t = map(int, input().strip().split(' '))
    edges = [[-1, -1, 0, 0] for _ in range(2 * m)]
    g = defaultdict(list)
    for i in range(m):
        x, y, w, cost = map(int, input().strip().split(' '))
        edges[i * 2] = [x - 1, y - 1, w, cost]
        g[x - 1].append(i * 2)
        edges[i * 2 + 1] = [y - 1, x - 1, 0, -cost]
        g[y - 1].append(i * 2 + 1)
    mysolve = solve(n, edges, g, s - 1, t - 1)
    f, c = mysolve.MCMF()
    print(f,c)


if __name__ == "__main__":
    main()


