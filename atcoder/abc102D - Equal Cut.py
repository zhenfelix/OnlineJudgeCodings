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
        # MOD = 998244353
        # n, m, k = list(map(int, input().split()))
        # st = input()
        n = int(input())
        arr = list(map(int, input().split()))
        # n = len(arr)
        # brr = list(map(int, input().split()))
        s1, s2, s3 =  0, arr[0], arr[1]+arr[2]
        s4 = sum(arr[3:])
        # print(s1, s2, s3, s4)
        left, right = -1, 2 
        ans = inf
        for mid in range(1,n-2):
            s2 += arr[mid]
            s3 -= arr[mid]
            lo = []
            while s1 <= s2 and left+1 < mid:
                if s1 > 0 and s2 > 0:
                    lo = [(s1,s2)]
                # lo = [(s1,s2)]
                left += 1
                s1 += arr[left]
                s2 -= arr[left]
            if s1 > 0 and s2 > 0:
                lo.append((s1,s2))
            if s1 > s2:
                s1 -= arr[left]
                s2 += arr[left]
                left -= 1
            # lo.append((s1,s2))
            hi = []
            while s3 <= s4 and right+1 < n-1:
                if s3 > 0 and s4 > 0:
                    hi = [(s3,s4)]
                # hi = [(s3,s4)]
                right += 1
                s3 += arr[right]
                s4 -= arr[right]
            if s3 > 0 and s4 > 0:
                hi.append((s3,s4))
            if s3 > s4:
                s3 -= arr[right]
                s4 += arr[right]
                right -= 1
            # hi.append((s3,s4))
            # print(s1, s2, s3, s4, left, mid, right)
            # print(lo,hi)
            for q1, q2 in lo:
                for q3, q4 in hi:
                    ans = min(ans, max(q1,q2,q3,q4)-min(q1,q2,q3,q4))
        return ans 



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


