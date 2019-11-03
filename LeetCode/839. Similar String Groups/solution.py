import itertools
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        m, n = len(A[0]), len(A)
        A = set(A)
        p, res = {s : s for s in A}, len(A) # p: parent
        def find(s):
            while s != p[s]: 
                p[s] = p[p[s]]
                s = p[s]
            return s
        def judge(a, b):
            cnt = 0
            for i, j in zip(a, b):
                if i != j:
                    if cnt < 2: cnt += 1
                    else: return False
            return cnt == 2
        if m > n:
            for a, b in itertools.combinations(A, 2): # O(m * n ^ 2)
                if judge(a, b):
                    ra, rb = find(a), find(b)
                    if ra != rb: res, p[ra] = res - 1, rb
        else: 
            for a in A: # O(n * m ^ 2)
                for i, j in itertools.combinations(range(m), 2):
                    b = a[:i] + a[j] + a[i + 1: j] + a[i] + a[j + 1:]
                    if b in A: 
                        ra, rb = find(a), find(b)
                        if ra != rb: res, p[ra] = res - 1, rb
        return res

# class Solution:
#     def numSimilarGroups(self, A: List[str]) -> int:
#         def find(x):
#             if x != parent[x]:
#                 parent[x] = find(parent[x])
#             return parent[x]
        
#         A = list(set(A))
#         n, m = len(A), len(A[0])
#         # print(n)
#         parent = [i for i in range(n)]

#         if m**2 < n:
#             mp = {}
#             for i in range(n):
#                 mp[A[i]] = i
#             for k in range(n):
#                 for i in range(m):
#                     for j in range(i+1,m):
#                         neighbor = A[k][:i]+A[k][j]+A[k][i+1:j]+A[k][i]+A[k][j+1:]
#                         idx = mp.get(neighbor,-1)
#                         if idx != k and idx != -1:
#                             parent[find(idx)] = find(k)

#         else:
#             for i in range(n):
#                 for j in range(i+1,n):
#                     diff = 0
#                     for k in range(m):
#                         if A[i][k] != A[j][k]:
#                             diff += 1
#                     if diff == 2:
#                         parent[find(j)] = find(i)
#         return len(set([find(i) for i in range(n)]))


# class DSU:
#     def __init__(self, N):
#         self.par = list(range(N))
#     def find(self, x):
#         if self.par[x] != x:
#             self.par[x] = self.find(self.par[x])
#         return self.par[x]
#     def union(self, x, y):
#         self.par[self.find(x)] = self.find(y)

# class Solution(object): # (NW) * min(N, W*W) complexity
#     def numSimilarGroups(self, A):
#         A = list(set(A))
#         N, W = len(A), len(A[0])
#         # print(N)

#         def similar(word1, word2):
#             diff = 0
#             for x, y in zip(word1, word2):
#                 if x != y:
#                     diff += 1
#             return diff <= 2

#         dsu = DSU(N)

#         if N < W*W: # If few words, then check for pairwise similarity: O(N^2 W)
#             for (i1, word1), (i2, word2) in \
#                     itertools.combinations(enumerate(A), 2):
#                 if similar(word1, word2):
#                     dsu.union(i1, i2)

#         else: # If short words, check all neighbors: O(N W^3)
#             buckets = collections.defaultdict(set)
#             for i, word in enumerate(A):
#                 L = list(word)
#                 for j0, j1 in itertools.combinations(range(W), 2):
#                     L[j0], L[j1] = L[j1], L[j0]
#                     buckets["".join(L)].add(i)
#                     L[j0], L[j1] = L[j1], L[j0]

#             for i1, word in enumerate(A):
#                 for i2 in buckets[word]:
#                     dsu.union(i1, i2)

#         return sum(dsu.par[x] == x for x in range(N))