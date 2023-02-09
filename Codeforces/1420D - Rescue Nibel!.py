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
# sys.setrecursionlimit(0x0FFFFFFF)
# threading.stack_size(0x04000000)

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
        MOD = 998244353
        n, k = list(map(int, input().split()))
        def quickmul(a, p):
            res = 1
            while p:
                if p&1:
                    res = (res*a)%MOD
                a = (a*a)%MOD
                p >>= 1
            return res 
        f = [1]*(n+1)
        for i in range(1,n+1):
            f[i] = (f[i-1]*i)%MOD
        invf = [1]*(n+1)
        invf[n] = quickmul(f[n], MOD-2)
        for i in range(n)[::-1]:
            invf[i] = (invf[i+1]*(i+1))%MOD
        def calc(x, y):
            return (f[x]*invf[y]*invf[x-y])%MOD

        # print(f, invf)
        # for i in range(k-1,n+1):
        #     print(i,k-1,calc(i,k-1))

        arr = []
        for _ in range(n):
            l, r = list(map(int, input().split()))
            arr.append((l,r))
        arr.sort()
        hq = []
        ans = 0
        for l, r in arr:
            while hq and hq[0] < l:
                heappop(hq)
            if len(hq) >= k-1:
                ans = (ans+calc(len(hq), k-1))%MOD 
            heappush(hq, r)
        return ans 

        


    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split())) 
        # solve()
        print(solve())
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
    # threading.Thread(target=main).start()


