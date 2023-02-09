class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n+1)]
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
            return

        for i in range(1+threshold,n+1):
            j = i*2 
            while j <= n:
                connect(i,j)
                j += i 
        ans = []
        for a, b in queries:
            ra, rb = find(a), find(b)
            ans.append(ra == rb)
        return ans 
                

# class Solution:
#     def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
#         parent = [i for i in range(n+1)]
#         def factor(y):
#             fs = []
#             for i in range(1,int(y**0.5)+1):
#                 if x%i == 0:
#                     if i > threshold:
#                         fs.append(i)
#                     if x//i > threshold:
#                         fs.append(x//i)
#             return fs 
#         def find(x):
#             if parent[x] != x:
#                 parent[x] = find(parent[x])
#             return parent[x]
#         def union(x,y):
#             rx, ry = find(x), find(y)
#             if rx != ry:
#                 parent[rx] = ry
#             return

#         for x in range(1,n+1):
#             fs = factor(x)
#             # print(x,fs)
#             if len(fs) > 1:
#                 for i in range(1,len(fs)):
#                     union(fs[i],fs[i-1])
#         res = []
#         # print(parent)
#         for a, b in queries:
#             ra, rb = find(a), find(b)
#             # print(a,b,ra,rb)
#             res.append(ra==rb)
#         return res 


# # Feel free to copy this class for later reuse!
# class UnionFind:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
#         self.size = [0] * n
#     def find(self, x):
#         if x != self.parent[x]:
#             self.parent[x] = self.find(self.parent[x]) # Path compression
#         return self.parent[x]
#     def union(self, u, v):
#         pu = self.find(u)
#         pv = self.find(v)
#         if self.size[pu] > self.size[pv]: # Union by larger size
#             self.size[pu] += self.size[pv]
#             self.parent[pv] = pu
#         else:
#             self.size[pv] += self.size[pu]
#             self.parent[pu] = pv

# class Solution(object):
#     def areConnected(self, n, threshold, queries):
#         uf = UnionFind(n+1)
#         for i in range(threshold+1, n+1):
#             for j in range(i*2, n+1, i): # step by i
#                 uf.union(i, j)
#         ans = []
#         for q in queries:
#             pa = uf.find(q[0])
#             pb = uf.find(q[1])
#             ans.append(pa == pb)
#         return ans


# Feel free to copy this class for later reuse!
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0] * n
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # Path compression
        return self.parent[x]
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if self.size[pu] > self.size[pv]: # Union by larger size
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv

class Solution(object):
    def areConnected(self, n, threshold, queries):
        uf = UnionFind(n+1)
        isPrime = [True]*(n+1)
        for i in range(threshold+1, n+1):
            if not isPrime[i]:
                continue
            for j in range(i*2, n+1, i): # step by i
                uf.union(i, j)
                isPrime[j] = False
        ans = []
        for q in queries:
            pa = uf.find(q[0])
            pb = uf.find(q[1])
            ans.append(pa == pb)
        return ans