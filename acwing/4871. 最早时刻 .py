import time
import bisect
import functools
import math
import os
import random
import re
import sys
import threading
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from io import BytesIO, IOBase
from itertools import accumulate, combinations, permutations
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase
from typing import *

BUFSIZE = 4096
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

sys.stdin = IOWrapper(sys.stdin)
sys.stdout = IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def I():
    return input()

def II():
    return int(input())

def MII():
    return map(int, input().split())

def LI():
    return list(input().split())

def LII():
    return list(map(int, input().split()))

def GMI():
    return map(lambda x: int(x) - 1, input().split())

def LGMI():
    return list(map(lambda x: int(x) - 1, input().split()))

inf = float('inf')

# from types import GeneratorType

# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc

# RANDOM = random.getrandbits(32)

# class Wrapper(int):
#     def __init__(self, x):
#         int.__init__(x)

#     def __hash__(self):
#         return super(Wrapper, self).__hash__() ^ RANDOM

n, m = MII()
path = [[] for _ in range(n)]
for _ in range(m):
    u, v, d = MII()
    u -= 1
    v -= 1
    path[u].append([v, d])
    path[v].append([u, d])

cannot = [None for _ in range(n)]
for i in range(n):
    _, *lst = LII()
    d = {}
    tmp = set(lst)
    for x in lst:
        if x + 1 not in tmp:
            d[x] = x + 1
            v = x
            while v - 1 in tmp:
                v -= 1
                d[v] = x + 1
    cannot[i] = d

dist = [inf] * n
dist[0] = 0
hpq = [[0, 0]]
while hpq:
    d, u = heappop(hpq)
    if dist[u] < d: continue
    for v, new_d in path[u]:
        tmp_d = d
        if tmp_d in cannot[u]:
            tmp_d = cannot[u][tmp_d]
        new_dist = tmp_d + new_d
        if new_dist < dist[v]:
            dist[v] = new_dist
            heappush(hpq, [new_dist, v])
ans = dist[-1]
print(ans if ans < inf else -1)

# 作者：小羊肖恩_1
# 链接：https://www.acwing.com/activity/content/code/content/5820595/
# 来源：AcWing
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



import os,sys, threading
from random import randint, shuffle
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
    from string import ascii_uppercase, ascii_lowercase
    def solve():
        # MOD = 998244353
        n, m = list(map(int, input().split()))
        g = defaultdict(list)
        for _ in range(m):
            a, b, c = list(map(int, input().split()))
            a -= 1
            b -= 1
            g[a].append((b,c))
            g[b].append((a,c))
        forbiden = [[] for _ in range(n)]
        dist = [[] for _ in range(n)]
        reach = [[] for _ in range(n)]
        for i in range(n):
            forbiden[i] = [-1]+list(map(int, input().split()))[1:]
            k = len(forbiden[i])
            dist[i] = [inf]*k
            reach[i] = [-1]*k
            for j in range(k)[::-1]:
                if j+1 == k or forbiden[i][j]+1 != forbiden[i][j+1]:
                    reach[i][j] = forbiden[i][j]+1
                else:
                    reach[i][j] = reach[i][j+1]
        
        hq = []
        k = len(forbiden[0])
        mi = inf
        for i in range(k):
            heappush(hq, (reach[0][i], 0, i))
            dist[0][i] = reach[0][i]
        while hq:
            d, i, j = heappop(hq)
            if i == n-1: return mi 
            if d > dist[i][j]: continue
            for ni, c in g[i]:
                nd = d+c 
                idx = bisect_right(forbiden[ni], nd)-1
                if ni == n-1: mi = min(mi,nd)
                nd = max(nd, reach[ni][idx])
                if nd < dist[ni][idx]:
                    dist[ni][idx] = nd 
                    heappush(hq, (nd,ni,idx))
        return -1
        


    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split())) 
        # solve()
        # _ = input()
        print(solve())
        # ans = solve()
        # if ans:
        #     for j in ans:
        #         print(j)  
        # else:
        #     print("impossible")
        # if solve():
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


