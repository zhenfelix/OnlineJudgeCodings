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

    def solve(n,arr):
        qh, qw = [], []
        for i, (h,w) in enumerate(arr):
            qh.append((-h,0,i))
            qw.append((-w,1,i))
        def check(q1,q2):
            visited = set()
            seq = []
            i = j = 0
            while i < n or j < n:
                while i < n and q1[i][-1] in visited:
                    i += 1
                if i >= n: break 
                cur = q1[i][0]
                while i < n:
                    if q1[i][0] != cur: break 
                    _, k, idx = q1[i]
                    if idx not in visited:
                        visited.add(idx)
                        seq.append((idx,k))
                    i += 1
                while j < n and q2[j][-1] in visited:
                    j += 1
                if j >= n: break
                cur = q2[j][0]
                while j < n:
                    if q2[j][0] != cur: break
                    _, k, idx = q2[j]
                    if idx not in visited:
                        visited.add(idx)
                        seq.append((idx,k))
                    j += 1
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
        
        
        qh.sort()
        qw.sort()
        res = set()
        tmp = check(qh,qw)
        if tmp: res.add(tuple(tmp))
        tmp = check(qw,qh)
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


