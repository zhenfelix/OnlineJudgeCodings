# class Solution:
#     def processQueries(self, queries: List[int], m: int) -> List[int]:
#         arr = [i+1 for i in range(m)]
#         res = []
#         for q in queries:
#             idx = arr.index(q)
#             res.append(idx)
#             arr = [arr[idx]] + arr[:idx] + arr[idx+1:]
#         return res

class Fenwick:
    def __init__(self, n):
        sz = 1
        while sz <= n:
            sz *= 2
        self.size = sz
        self.data = [0] * sz

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i

class Solution(object):
    def processQueries(self, queries, n):
        fenw = Fenwick(2 * n)
        vimap = {}
        for i in range(1, n + 1):
            fenw.add(i + n, 1)
            vimap[i] = i + n
        cur = n
        
        ans = []
        for q in queries:
            i = vimap.pop(q)
            rank = fenw.sum(i)-1
            # rank = fenw.sum(i-1)
            ans.append(rank)
            
            vimap[q] = cur
            fenw.add(i, -1)
            fenw.add(cur, 1)
            cur -= 1
        return ans