import os,sys, threading
from random import randint, shuffle
from io import BytesIO, IOBase

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop, heapify
from functools import lru_cache, reduce
from itertools import accumulate, permutations
import math, copy


# sys.setrecursionlimit(2**20)
# threading.stack_size(2**20)
sys.setrecursionlimit(0x0FFFFFFF)
threading.stack_size(0x08000000)

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

MOD = 998244353  
from math import * 


def main():
    # def quickmul(a, p):
    #     res = 1
    #     while p:
    #         if p&1:
    #             res = (res*a)%MOD
    #         p >>= 1
    #         a = (a*a)%MOD
    #     return res 

    def query(tree, x):
        s = 0
        while x:
            s = (tree[x]+s)
            x -= x&-x 
        return s 
    def update(tree, x, v):
        while x < len(tree):
            tree[x] = (tree[x]+v)
            x += x&-x 
        return 

    def solve():
        n, m, q = list(map(int, input().split()))
        A = [0]*n 
        B = [0]*m 
        qs = []
        av, bv = set([0]), set([0])
        for _ in range(q):
            t, x, y = list(map(int, input().split()))
            x -= 1
            if t == 1:
                av.add(y)
            else:
                bv.add(y)
            qs.append((t,x,y))
        av = sorted(list(av))
        bv = sorted(list(bv))
        mxa, mxb = len(av), len(bv)
        mpa = {v: i for i, v in enumerate(av)}
        mpb = {v: i for i, v in enumerate(bv)}

        cnta, suma = [0]*(mxa+5), [0]*(mxa+5)
        cntb, sumb = [0]*(mxb+5), [0]*(mxb+5)
        update(cnta, mpa[0]+1, n)
        update(cntb, mpb[0]+1, m)
        ans = 0
        for t, x, y in qs:
            if t == 1:
                v = A[x]
                idx = bisect_right(bv,v)
                ans -= query(cntb, idx)*v
                ans -= (query(sumb, mxb)-query(sumb, idx))
                idx = bisect_right(bv,y)
                ans += query(cntb, idx)*y
                ans += (query(sumb, mxb)-query(sumb, idx))
                idx = mpa[v]+1
                update(cnta, idx, -1)
                update(suma, idx, -v)
                idx = mpa[y]+1
                update(cnta, idx, 1)
                update(suma, idx, y)
                A[x] = y
            else:
                v = B[x]
                idx = bisect_right(av,v)
                ans -= query(cnta, idx)*v
                ans -= (query(suma, mxa)-query(suma, idx))
                idx = bisect_right(av,y)
                ans += query(cnta, idx)*y
                ans += (query(suma, mxa)-query(suma, idx))
                idx = mpb[v]+1
                update(cntb, idx, -1)
                update(sumb, idx, -v)
                idx = mpb[y]+1
                update(cntb, idx, 1)
                update(sumb, idx, y)
                B[x] = y
            print(ans)
        return  



    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split())) 
        solve()
        # print(solve())
        # if solve():
        #     print("YA")   
        # else:
        #     print("TIDAK")
        # print(solve())
        # n = int(input())
        # arr = list(map(int, input().split()))     
        # if solve(n, m, k):
        #     print("YES")
        # else:
        #     print("NO")


    # debug(ans)


if __name__ == "__main__":
    # main()
    threading.Thread(target=main).start()


