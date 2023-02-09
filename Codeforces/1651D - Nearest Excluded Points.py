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
        n = int(input())
        points = set()
        boundary = set()
        arr = []
        for _ in range(n):
            x, y = list(map(int, input().split()))
            points.add((x,y))
            arr.append((x,y))

        dxy = [-1,0,1,0,-1]
        for x, y in points:
            for dx, dy in zip(dxy[1:],dxy[:-1]):
                dx += x 
                dy += y 
                if (dx,dy) not in boundary and (dx,dy) not in points:
                    boundary.add((dx,dy))

        mp = dict()
        q = [(x,y,x,y) for x, y in boundary]
        while q:
            nq = []
            for rx, ry, x, y in q:
                for dx, dy in zip(dxy[1:], dxy[:-1]):
                    dx += x 
                    dy += y 
                    if (dx,dy) not in mp and (dx,dy) in points:
                        mp[dx,dy] = (rx,ry)
                        nq.append((rx,ry,dx,dy))
            q = nq 
        for x, y in arr:
            print(*mp[x,y])

        return 

        


    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split())) 
        solve()
        # print(solve())
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






#TLE
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
        n = int(input())
        seen = set()
        arr = []
        diag, antidiag = dict(), dict()
        for _ in range(n):
            x, y = list(map(int, input().split()))
            seen.add((x,y))
            arr.append((x,y))
            diag[x,y] = (x+1,y+1)
            antidiag[x,y] = (x+1,y-1)
        for x, y in sorted(arr, reverse = True):
            if (x+1,y+1) in diag:
                diag[x,y] = diag[x+1,y+1]
            if (x+1,y-1) in antidiag:
                antidiag[x,y] = antidiag[x+1,y-1]
        def check(x,y,limit,mp):
            if (x,y) not in mp:
                print(x,y)
                return True 
            lx, ly = mp[x,y]
            if lx <= limit:
                print(lx,ly)
                return True 
            return False 
        for x, y in arr:
            delta = 1
            while True:
                if check(x,y-delta,x+delta,diag):
                    break 
                if check(x-delta,y,x,diag):
                    break
                if check(x,y+delta,x+delta,antidiag):
                    break
                if check(x-delta,y,x,antidiag):
                    break
                delta += 1
        return 

        


    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split())) 
        solve()
        # print(solve())
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


