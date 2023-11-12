import sys,os

# sys.stdin = open("input","r") 

input = sys.stdin.readline


from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *
from math import *
from string import ascii_lowercase

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

MOD = 10**9+7
def solve():
    n, m = list(map(int, input().split()))
    g = defaultdict(list)
    for _ in range(m):
        u, v = list(map(int, input().split()))
        g[u].append(v)
        g[v].append(u)
    hq = [1]
    visited = set([1])
    ans = []
    while hq:
        cur = heappop(hq)
        ans.append(cur)
        for nxt in g[cur]:
            if nxt not in visited:
                visited.add(nxt)
                heappush(hq,nxt)
    print(*ans)
    return



# t = int(input())
t = 1
for _ in range(t):
    solve()
