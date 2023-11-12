import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *
from math import *
from string import ascii_lowercase

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

MOD = 10**9+7
def solve():
    n, m, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    brr = sorted(arr)
    g = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        edges.append((u,v))


    def check(target):
        tmp = [0]*n
        for u,v in edges:
            if arr[u] <= target and arr[v] <= target:
                tmp[v] += 1
        q = []
        for i in range(n):
            if tmp[i] == 0 and arr[i] <= target:
                q.append(i)
        cnt = 0
        while q:
            nq = []
            cnt += 1
            if cnt >= k:
                return True
            for cur in q:
                for nxt in g[cur]:
                    if arr[nxt] > target: continue
                    tmp[nxt] -= 1
                    if tmp[nxt] == 0:
                        nq.append(nxt)
            q = nq 
        for i in range(n):
            if tmp[i] > 0 and arr[i] <= target:
                return True
        return False

         
    lo, hi = 0, n-1
    while lo <= hi:
        t = (lo+hi)//2
        if check(brr[t]):
            hi = t-1
        else:
            lo = t+1
    print(brr[lo] if lo < n else -1)
    return 


# t = int(input())
t = 1
for _ in range(t):
    solve()
