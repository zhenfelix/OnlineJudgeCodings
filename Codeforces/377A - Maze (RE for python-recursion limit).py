import os,sys,resource
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
        n, m, k = list(map(int, input().split()))
        mat = []
        for _ in range(n):
            s = input()
            mat.append(list(s))
        dij = [-1,0,1,0,-1]
        visited = set()
        def dfs(i, j):
            nonlocal k 
            if k == 0 or i < 0 or i >= n or j < 0 or j >= m or mat[i][j] == '#':
            # if (i,j) in visited or i < 0 or i >= n or j < 0 or j >= m or mat[i][j] == '#':
                return 0
            visited.add((i,j))
            # print(i,j)
            cnt = 0
            for di, dj in zip(dij[:-1],dij[1:]):
                di += i 
                dj += j 
                if (di,dj) in visited:
                    continue
                cnt += dfs(di,dj)
            if cnt == 0 and k > 0:
                k -= 1
                mat[i][j] = 'X'
                return 0
            return 1
        flag = False
        for x in range(n):
            for y in range(m):
                if not flag and mat[x][y] == '.':
                    dfs(x,y)
                    flag = True

        for s in mat:
            print(''.join(s))
        return

                
        
        


    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split()))     
        solve()
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


