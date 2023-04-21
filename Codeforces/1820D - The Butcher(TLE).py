# list copy causes TLE
import os,sys, threading
from random import *
from io import BytesIO, IOBase

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop, heapify
from functools import lru_cache, reduce
from itertools import accumulate, permutations
import math, copy


# sys.setrecursionlimit(2*10**5)
# threading.stack_size(2**30)
# sys.setrecursionlimit(0x0FFFFFFF)
# threading.stack_size(0x08000000)

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

    # def query(tree, x):
    #     s = 0
    #     while x:
    #         s = (tree[x]+s)
    #         x -= x&-x 
    #     return s 
    # def update(tree, x, v):
    #     while x < len(tree):
    #         tree[x] = (tree[x]+v)
    #         x += x&-x 
    #     return         
    def solve(n,arr):
        # MOD = 998244353
        qh, qw = [], []
        for i, (h,w) in enumerate(arr):
            qh.append((-h,0,i))
            qw.append((-w,1,i))
        def check(q1,q2):
            visited = set()
            seq = []
            # heapify(q1)
            # heapify(q2)
            while q1 or q2:
                while q1 and q1[0][-1] in visited:
                    heappop(q1)
                if not q1: break 
                cur = q1[0][0]
                while q1:
                    if q1[0][0] != cur: break 
                    _, k, i = heappop(q1)
                    if i not in visited:
                        visited.add(i)
                        seq.append((i,k))
                while q2 and q2[0][-1] in visited:
                    heappop(q2)
                if not q2: break
                cur = q2[0][0]
                while q2:
                    if q2[0][0] != cur: break
                    _, k, i = heappop(q2)
                    if i not in visited:
                        visited.add(i)
                        seq.append((i,k))
            if len(seq) < n: return []
            seq = seq[::-1]
            ans = [0,0]
            si,sk = seq[0]
            ans[sk] = arr[si][sk]
            for i,k in seq:
                if arr[i][k] == ans[k]:
                    ans[1-k] += arr[i][1-k]
                elif arr[i][1-k] == ans[1-k]:
                    ans[k] += arr[i][k]
                else:
                    return []
            return ans 
        
        res = set()
        heapify(qh)
        heapify(qw)
        tmp = check(qh.copy(),qw.copy())
        if tmp: res.add(tuple(tmp))
        tmp = check(qw.copy(),qh.copy())
        if tmp: res.add(tuple(tmp))
        print(len(res))
        for h,w in res:
            print(h,w)
        return  
        
    # sys.stdin = open('contests/input', 'r')
    t = int(input())
    # t = 1
    for i in range(t):
        n = int(input())
        # n, c, d = list(map(int, input().split())) 
        arr = []
        for _ in range(n):
            h, w = list(map(int, input().split())) 
            arr.append((h,w))
        
        solve(n,arr)
       
        # print(solve())

        # if solve(n,arr):
        #     print("Yes")   
        # else:
        #     print("No")
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


