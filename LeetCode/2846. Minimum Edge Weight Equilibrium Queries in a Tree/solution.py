class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        W, K = 27, 20 
        parent = [[-1]*K for _ in range(n)]
        cnt = [[0]*W for _ in range(n)]
        g = defaultdict(list)
        tin = [-1]*n 
        tout = [-1]*n 
        clock = 0
        for u, v, w in edges:
            g[u].append((v,w))
            g[v].append((u,w))
        def dfs(cur,pre):
            nonlocal clock
            tin[cur] = clock
            clock += 1
            parent[cur][0] = pre 
            for nxt, w in g[cur]:
                if nxt == pre: continue
                cnt[nxt] = cnt[cur][:]
                cnt[nxt][w] += 1
                dfs(nxt,cur)
            clock += 1
            tout[cur] = clock
            return 
        dfs(0,0)
        for k in range(1,K):
            for i in range(n):
                parent[i][k] = parent[parent[i][k-1]][k-1]
        def isAncestor(u,v):
            return tin[u] <= tin[v] and tout[u] >= tout[v]
        ans = []
        # print(cnt)
        for a, b in queries:
            if isAncestor(a,b) or isAncestor(b,a):
                if isAncestor(b,a): a, b = b, a 
                tmp = [cnt[b][w]-cnt[a][w] for w in range(W)]
                cur = tot = sum(tmp)
                for w in range(W):
                    cur = min(cur, tot-tmp[w])
                ans.append(cur)
            else:
                p = a  
                for k in range(K)[::-1]:
                    if not isAncestor(parent[p][k],b):
                        p = parent[p][k]
                p = parent[p][0]
                tmp = [cnt[a][w]-cnt[p][w]+cnt[b][w]-cnt[p][w] for w in range(W)]
                cur = tot = sum(tmp)
                # print(a,b,p,tot)
                # for w in range(W):
                #     print(cnt[a][w],cnt[b][w],cnt[p][w])
                for w in range(W):
                    cur = min(cur, tot-tmp[w])
                ans.append(cur)
        return ans 



from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
from typing import *

"""
There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a
2D integer array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates that there is an
edge between nodes ui and vi with weight wi in the tree.

You are also given a 2D integer array queries of length m, where queries[i] = [ai, bi]. For each
query, find the minimum number of operations required to make the weight of every edge on the path
from ai to bi equal. In one operation, you can choose any edge of the tree and change its weight to
any value.

Note that:

 * Queries are independent of each other, meaning that the tree returns to its initial state on each
   new query.
 * The path from ai to bi is a sequence of distinct nodes starting with node ai and ending with node
   bi such that every two adjacent nodes in the sequence share an edge in the tree.

Return an array answer of length m where answer[i] is the answer to the ith query.

 

Example 1:

[https://assets.leetcode.com/uploads/2023/08/11/graph-6-1.png]


Input: n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]
Output: [0,0,1,3]
Explanation: In the first query, all the edges in the path from 0 to 3 have a weight of 1. Hence, the answer is 0.
In the second query, all the edges in the path from 3 to 6 have a weight of 2. Hence, the answer is 0.
In the third query, we change the weight of edge [2,3] to 2. After this operation, all the edges in the path from 2 to 6 have a weight of 2. Hence, the answer is 1.
In the fourth query, we change the weights of edges [0,1], [1,2] and [2,3] to 2. After these operations, all the edges in the path from 0 to 6 have a weight of 2. Hence, the answer is 3.
For each queries[i], it can be shown that answer[i] is the minimum number of operations needed to equalize all the edge weights in the path from ai to bi.


Example 2:

[https://assets.leetcode.com/uploads/2023/08/11/graph-9-1.png]


Input: n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]
Output: [1,2,2,3]
Explanation: In the first query, we change the weight of edge [1,3] to 6. After this operation, all the edges in the path from 4 to 6 have a weight of 6. Hence, the answer is 1.
In the second query, we change the weight of edges [0,3] and [3,1] to 6. After these operations, all the edges in the path from 0 to 4 have a weight of 6. Hence, the answer is 2.
In the third query, we change the weight of edges [1,3] and [5,2] to 6. After these operations, all the edges in the path from 6 to 5 have a weight of 6. Hence, the answer is 2.
In the fourth query, we change the weights of edges [0,7], [0,3] and [1,3] to 6. After these operations, all the edges in the path from 7 to 4 have a weight of 6. Hence, the answer is 3.
For each queries[i], it can be shown that answer[i] is the minimum number of operations needed to equalize all the edge weights in the path from ai to bi.


 

Constraints:

 * 1 <= n <= 104
 * edges.length == n - 1
 * edges[i].length == 3
 * 0 <= ui, vi < n
 * 1 <= wi <= 26
 * The input is generated such that edges represents a valid tree.
 * 1 <= queries.length == m <= 2 * 104
 * queries[i].length == 2
 * 0 <= ai, bi < n
"""

MOD = 1000000007 # 998244353

class JumpOnTree:
    def __init__(self, edges, root=0):
        self.n = len(edges)
        self.edges = edges
        self.root = root
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1] * self.n
        self.depth[self.root] = 0
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.book = [[0] * 26 for _ in range(self.n)]
        self.dfs()
        self.doubling()

    def dfs(self):
        stack = [self.root]
        while stack:
            u = stack.pop()
            for v, w in self.edges[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    stack.append(v)
                    self.book[v] = self.book[u].copy()
                    self.book[v][w] += 1

    def doubling(self):
        for i in range(1, self.logn):
            for u in range(self.n):
                p = self.parent[i - 1][u]
                if p != -1:
                    self.parent[i][u] = self.parent[i - 1][p]

    def lca(self, u, v):
        du = self.depth[u]
        dv = self.depth[v]
        if du > dv:
            du, dv = dv, du
            u, v = v, u

        d = dv - du
        i = 0
        while d > 0:
            if d & 1:
                v = self.parent[i][v]
            d >>= 1
            i += 1
        if u == v:
            return u

        logn = (du - 1).bit_length()
        for i in range(logn - 1, -1, -1):
            pu = self.parent[i][u]
            pv = self.parent[i][v]
            if pu != pv:
                u = pu
                v = pv
        return self.parent[0][u]

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w - 1))
            g[v].append((u, w - 1))
        
        jt = JumpOnTree(g)
        
        res = []
        for u, v in queries:
            lca = jt.lca(u, v)
            cnt = [a + b - c * 2 for a, b, c in zip(jt.book[u], jt.book[v], jt.book[lca])]
            tot = sum(cnt)
            mx = max(cnt)
            res.append(tot - mx)
        return res

testcases = [
    # [7, [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], [[0,3],[3,6],[2,6],[0,6]]],
    # [],
]

s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)

for args in testcases:
    print(func(*args))