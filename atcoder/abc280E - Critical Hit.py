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
    def quickmul(a, p):
        res = 1
        while p:
            if p&1:
                res = (res*a)%MOD
            p >>= 1
            a = (a*a)%MOD
        return res 

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

    def solve():
        # MOD = 998244353
        n, p0 = list(map(int, input().split()))
        # st = input()
        # k = int(input())
        # arr = list(map(int, input().split()))
        # brr = list(map(int, input().split()))
        
        y = quickmul(100,(MOD-2))
        s = 0
        p = 1
        for i in range(n):
            s = (s+p)%MOD 
            p = (1-p*p0*y)%MOD 


        return s
        

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split())) 
        # solve()
        print(solve())
        # ans = solve()
        # if ans:
        #     for j in ans:
        #         print(j)  
        # else:
        #     print("impossible")
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
    # main()
    threading.Thread(target=main).start()




import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc

n, p = list(map(int,input().split()))
MOD = 998244353
memo = dict()
@bootstrap
# @lru_cache(None)
def dfs(cur):
    if cur <= 0:
        yield 0 
    if cur in memo:
        yield memo[cur]
    a = yield dfs(cur-2)
    b = yield dfs(cur-1)
    res = (a+1)*p+(b+1)*(100-p)
    memo[cur] = res*pow(100,-1,MOD)%MOD 
    yield memo[cur]
print(dfs(n))



m = 998244353
def mm(a, b):
    c = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(c)):
        for j in range(len(c[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= m
    return c
def solve():
    n, p = list(map(int, input().strip().split()))
    if n < 2:
        return print(n)
    iv100 = pow(100, m - 2, m)
    q = (100 - p) * iv100 % m
    p = p * iv100 % m
    n -= 1
    r = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    a = [[q, 1, 0], [p, 0, 0], [1, 0, 1]]
    while n:
        if n & 1:
            r = mm(r, a)
        n >>= 1
        a = mm(a, a)
    print((r[0][0] + r[2][0]) % m)
    return 0

# for t in range(RI()[0] - 1):
#     solve()
solve()