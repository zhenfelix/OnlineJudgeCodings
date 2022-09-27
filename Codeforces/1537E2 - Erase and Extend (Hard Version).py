# https://www.luogu.com.cn/blog/zankizero/ti-xie-cf1537e2-erase-and-extend-hard-version#
import os,sys
from random import randint, shuffle
from io import BytesIO, IOBase

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop, heapify
from functools import lru_cache, reduce
from itertools import accumulate, permutations
import math, copy


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



def main():

    def solve(k):
        s = input()
        n = len(s)
        cnt = 1
        for i in range(1,n):
            if s[i] > s[i%cnt]:
                break 
            elif s[i] < s[i%cnt]:
                cnt = i+1
        s = s[:cnt]
        while len(s) < k:
            s = s+s 
        return s[:k]



    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        n, k = list(map(int, input().split()))     
        print(solve(k))   
        # n = int(input())
        # arr = list(map(int, input().split()))     
        # if solve(n, m, k):
        #     print("YES")
        # else:
        #     print("NO")


    # debug(ans)


if __name__ == "__main__":
    main()




# z function solution

def main():

    def zfunction(s) -> int:
        n = len(s)
        z = [0]*n 
        left, right = 0, 0 
        for i in range(1,n//2):
            if i <= right:
                z[i] = min(z[i-left], right-i+1)
            while i+z[i] < n and s[z[i]] == s[i+z[i]]:
                z[i] += 1
            if i+z[i]-1 > right:
                left, right = i, i+z[i]-1
        return z

    def solve(k):
        s = input()
        n = len(s)
        s = s+s
        z = zfunction(s)
        # print(z)
        cnt = 1
        for i in range(1,n):
            if z[i] < i and s[z[i]%cnt] < s[i+z[i]]:
                break 
            cnt += 1
        res = ['']*k 
        # print(cnt)
        for i in range(k):
            res[i] = s[i%cnt]
        return ''.join(res)



    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        n, k = list(map(int, input().split()))     
        print(solve(k))   
        # n = int(input())
        # arr = list(map(int, input().split()))     
        # if solve(n, m, k):
        #     print("YES")
        # else:
        #     print("NO")


    # debug(ans)


if __name__ == "__main__":
    main()


