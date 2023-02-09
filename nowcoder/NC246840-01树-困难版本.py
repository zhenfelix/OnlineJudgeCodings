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

# MOD = 998244353  
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

    def solve():
        MOD = 998244353
        # x, y = list(map(int, input().split()))
        # st = input()
        n = int(input())
        # arr = list(map(int, input().split()))
        # brr = list(map(int, input().split()))
        mat = [[0]*(n+1) for _ in range(n+1)]
        dxy = [[0,1],[1,0],[0,-1],[-1,0]]
        pdxy = [[-1,1],[1,1],[1,-1],[-1,-1]]
        q = deque([(0,0,0)])
        mat[0][0] = 1
        cnt = 1
        def check(x,y,k):
            dx, dy = dxy[k]
            if 0 <= x+dx*2 < n and 0 <= y+dy*2 < n+1 and mat[x+dx*2][y+dy*2] == 0:
                x += dx 
                y += dy 
                mat[x][y] = 1
                return x, y, k 
            k = (k+1)%4
            dx, dy = dxy[k]
            if 0 <= x+dx*2 < n and 0 <= y+dy*2 < n+1 and mat[x+dx*2][y+dy*2] == 0:
                x += dx 
                y += dy 
                mat[x][y] = 1
                return x, y, k
            return -1, -1, -1
        px, py, pk = -1, -1, -1
        while q:
            if cnt >= (n*n)//2+1:
                break
            x, y, k = q.popleft()
            px, py, pk = x, y, k
            x, y, k = check(x,y,k)
            if k == -1:
                continue
            q.append((x,y,k))
            cnt += 1
        # print(cnt)
        # print(px, py, pk)
        # print(x, y, k)
        # x, y = n//2, n//2+1
        while 0 <= px < n and 0 <= py < n:
            mat[px][py] ^= 1
            # print(px,py)
            pdx, pdy = pdxy[pk]
            px += pdx 
            py += pdy 
        for line in mat[:-1]:
            print(''.join(map(str,line[:-1])))
        return 
        

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split())) 
        solve()
        # print(solve())
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


