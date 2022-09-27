import os,sys
from random import randint, shuffle
from io import BytesIO, IOBase

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop, heapify
from functools import lru_cache, reduce
from itertools import accumulate, permutations
import math, copy


# sys.setrecursionlimit(3*10**5)
# resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])


# Fast IO Region
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# MOD = 998244353  
from math import * 


def main():
    def solve():
        n, m = list(map(int, input().split()))

        parent = [i for i in range(n)]
        sz = [1]*n 
        
        # def find(u):
        #     tmp = u
        #     while parent[u] != u:
        #         u = parent[u]
        #     root = u
        #     u = tmp
        #     while parent[u] != u:
        #         tmp = parent[u]
        #         parent[u] = root
        #         u = tmp 
        #     return root
        # def connect(u,v):
        #     ru, rv = find(u), find(v)
        #     inc = 0
        #     if ru != rv:
        #         inc = sz[ru]*sz[rv]
        #         parent[ru] = rv 
        #         sz[rv] += sz[ru]
        #     return inc

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u,v):
            ru, rv = find(u), find(v)
            inc = 0
            if ru != rv:
                inc = sz[ru]*sz[rv]
                if sz[ru] > sz[rv]:
                    parent[rv] = ru 
                    sz[ru] += sz[rv]
                else:
                    parent[ru] = rv
                    sz[rv] += sz[ru]
            return inc


        edges = []
        for _ in range(n-1):
            u, v, w = list(map(int, input().split()))
            edges.append((w,u-1,v-1))
        heapify(edges)
        qs = list(map(int, input().split()))
        ans = [0]*m 
        cur = 0
        idx = list(range(m))
        for i in sorted(idx, key = lambda x: qs[x]):
            q = qs[i]
            while edges and edges[0][0] <= q:
                w, u, v = heappop(edges)
                cur += connect(u,v)
            ans[i] = cur
        print(*ans)
        return 

        


    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split())) 
        solve()
        # if solve():
        #     print("YES")   
        # else:
        #     print("NO")
        # print(solve())
        # n = int(input())
        # arr = list(map(int, input().split()))     
        # if solve(n, m, k):
        #     print("YES")
        # else:
        #     print("NO")


    # debug(ans)


if __name__ == "__main__":
    main()


