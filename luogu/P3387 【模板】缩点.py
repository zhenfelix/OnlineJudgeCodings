import sys, heapq
from collections import *
import sys
sys.setrecursionlimit(10**6)


class solve:
    def __init__(self, n, edges, arr):
        self.arr = arr
        self.g = defaultdict(list)
        self.n = n
        for u, v in edges:
            self.g[u].append(v)
        self.tarjan()
        self.dag = defaultdict(list)
        self.indegree = defaultdict(int)
        for u, v in edges:
            u, v = self.component[u], self.component[v]
            if u != v:
                self.dag[u].append(v)
                self.indegree[v] += 1


    def tarjan(self):
        n = self.n
        self.level = [-1]*n
        self.lowlink = [-1]*n
        self.st = []
        self.onstack = [False]*n
        self.idx = 0
        self.component = [-1]*n
        self.weight = defaultdict(int)
        for i in range(n):
            if self.level[i] == -1:
                self.dfs(i)

    def dfs(self, s):
        self.idx += 1
        self.lowlink[s] = self.level[s] = self.idx
        self.st.append(s)
        self.onstack[s] = True
        for nxt in self.g[s]:
            if self.level[nxt] == -1:
                self.dfs(nxt)
                self.lowlink[s] = min(self.lowlink[s], self.lowlink[nxt])
            elif self.onstack[nxt]:
                self.lowlink[s] = min(self.lowlink[s], self.lowlink[nxt])
        if self.lowlink[s] == self.level[s]:
            while True:
                cur = self.st.pop()
                self.component[cur] = self.level[s]
                self.weight[self.component[cur]] += self.arr[cur]
                self.onstack[cur] = False
                if cur == s:
                    break

    def calc(self):
        res = -float('inf')
        dp = defaultdict(int)
        q = deque()
        for s in self.weight:
            if self.indegree[s] == 0:
                q.append(s)
                dp[s] = self.weight[s]
        while q:
            cur = q.popleft()
            res = max(res,dp[cur])
            for nxt in self.dag[cur]:
                dp[nxt] = max(dp[nxt], dp[cur]+self.weight[nxt])
                self.indegree[nxt] -= 1
                if self.indegree[nxt] == 0:
                    q.append(nxt)
        return res

def main():
    # sys.stdin = open('input.txt', 'r')
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    edges = []
    for _ in range(m):
        x, y = map(int, input().strip().split(' '))
        edges.append((x-1,y-1))
    # print(n,m)
    # print(arr)
    # print(edges)
    mysolve = solve(n,edges,arr)
    print(mysolve.calc())


if __name__ == "__main__":
    main()


