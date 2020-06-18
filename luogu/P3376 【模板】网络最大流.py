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


