# class TreeAncestor:

#     def __init__(self, n: int, parent: List[int]):
#         g = defaultdict(list)
#         for i, p in enumerate(parent):
#             g[p].append(i)
#         self.fa = defaultdict(list)
#         def dfs(cur,p,depth):
#             i = 0
#             while (1<<i) <= depth:
#                 if i == 0:
#                     self.fa[cur].append(p)
#                 else:
#                     self.fa[cur].append(self.fa[self.fa[cur][i-1]][i-1])
#                 i += 1
#             for nxt in g[cur]:
#                 dfs(nxt,cur,depth+1)
#             return

#         dfs(0,-1,0)
#         return


        

#     # def getKthAncestor(self, node: int, k: int) -> int:
#     #     if k == 0:
#     #         return node
#     #     step = k - (k&(k-1))
#     #     i = 0
#     #     while (1<<i) <= step:
#     #         i += 1
#     #     if i > len(self.fa[node]):
#     #         return -1
#     #     return self.getKthAncestor(self.fa[node][i-1],k-step)

#     def getKthAncestor(self, node: int, k: int) -> int:
#         cur, i = node, 0
#         while k:
#             if k & (1<<i):
#                 if i >= len(self.fa[cur]):
#                     return -1
#                 cur = self.fa[cur][i]
#                 k -= (1<<i)
#             i += 1

#         return cur


class TreeAncestor(object):
    
    def __init__(self, n, A):
        self.step = 15
        A = dict(enumerate(A))
        jump = [A]
        for s in range(self.step):
            B = {}
            for i in A:
                if A[i] in A:
                    B[i] = A[A[i]]
            jump.append(B)
            A = B
        self.jump = jump

    def getKthAncestor(self, x, k):
        step = self.step
        while k > 0 and x > -1:
            if k >= 1 << step:
                x = self.jump[step].get(x, -1)
                k -= 1 << step
            else:
                step -= 1
        return x


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        m = 1 + int(log2(n)) #at most 16 for this problem 
        self.dp = [[-1] * m for _ in range(n)] #ith node's 2^j parent
        for i in range(n): 
            self.dp[i][0] = parent[i] #2^0 parent
        for j in range(1, m):
            for i in range(n):
                if self.dp[i][j-1] != -1: 
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1: 
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node 