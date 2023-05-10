import os,sys, threading
from random import *
from io import BytesIO, IOBase

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop, heapify
from functools import lru_cache, reduce
from itertools import accumulate, permutations
import math, copy


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
MOD = 10**9+7
from math import * 


def main():
    def quickmul(a,q):
        b = 1
        while q:
            if q&1:
                b = (b*a)%MOD 
            a = (a*a)%MOD 
            q >>= 1
        return b 
    
    def solve():
        n, k = list(map(int, input().split()))
        g = defaultdict(list)
        for _ in range(n-1):
            u, v = list(map(int, input().split()))
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
        if k&1: return 1
        cnt = [1]*n 
        @bootstrap
        def dfs(cur,pre):
            ss = 0
            for nxt in g[cur]:
                if nxt == pre: continue
                ss += yield dfs(nxt,cur)
                ss += cnt[nxt]
                cnt[cur] += cnt[nxt]
            yield ss 
        tot = dfs(0,0)
        ans = 0
        @bootstrap
        def calc(cur,pre,D):
            nonlocal ans 
            ans += D+n-1
            for nxt in g[cur]:
                if nxt == pre: continue
                d = D 
                d += n-cnt[nxt]
                d -= cnt[nxt]
                yield calc(nxt,cur,d)
            yield
        calc(0,0,tot)

        return (ans*quickmul(n*(n-1),MOD-2))%MOD 

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # s = input()
        print(solve())
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


