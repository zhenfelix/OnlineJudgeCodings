# https://www.luogu.com.cn/problem/T122085?contestId=27163
# https://www.luogu.com.cn/blog/12cow/SBCOI2020

import sys, heapq
from collections import *

# sys.stdin = open('input.txt', 'r')
n, m, query = map(int, input().split(' '))
graph = defaultdict(list)
indegree = defaultdict(int)
for i in range(m):
    a, b = map(int, input().split(' '))
    graph[b].append(a)
    indegree[a] += 1

for i in range(query):
    start, end = map(int, input().split(' '))
    cntindegree = defaultdict(int)
    dp = [0] * (n + 1)
    q = deque()
    for j in range(1,n+1):
        if indegree[j] == 0 or j == end:
            dp[j] = -1
            q.append(j)

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dp[nxt] != 0:
                continue
            if dp[cur] == -1:
                dp[nxt] = 1
                q.append(nxt)
            else:
                cntindegree[nxt] += 1
                if indegree[nxt] == cntindegree[nxt]:
                    dp[nxt] = -1
                    q.append(nxt)
    print(dp[start])






