import os,sys
from random import randint, shuffle
from io import BytesIO, IOBase

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
from functools import lru_cache
from itertools import accumulate, permutations
import math

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



def main():

    def solve(n,m):
        arr = []
        cnt = 0
        for _ in range(n):
            s = input()
            cnt += s.count('0')
            arr.append(s)
        
        flag = False
        delta = [(0,-1),(-1,0),(0,1),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        for i in range(n):
            for j in range(m):
                if arr[i][j] == '0':
                    for dx, dy in delta:
                        dx += i 
                        dy += j 
                        if 0 <= dx < n and 0 <= dy < m and arr[dx][dy] == '0':
                            flag = True 
                            break
        if flag:
            return n*m-cnt 
        if cnt > 0:
            return n*m-cnt-1
        return n*m-2

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    t = int(input())
    # t = 1
    for _ in range(t):
        n, m = list(map(int, input().split()))
        print(solve(n,m))


    # debug(ans)


if __name__ == "__main__":
    main()


