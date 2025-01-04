import sys,os

# sys.stdin = open("input","r") 

input = sys.stdin.readline


from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *
# from math import *
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

from math import *
MOD = 10**9+7
def solve(idx):
    n,k = list(map(int, input().split()))
    g = defaultdict(list)
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    lo, hi = 1, (n-1)//(k+1)+1
    while lo <= hi:
        m = (lo+hi)//2
        cnt = [0]
        @bootstrap
        def dfs(cur,pre):
            s = 1
            for nxt in g[cur]:
                if nxt == pre: continue
                s += yield dfs(nxt,cur)
            if s >= m:
                cnt[0] += 1
                yield 0
            yield s 
        dfs(0,0)
        if cnt[0] >= k+1:
            lo = m+1
        else:
            hi = m-1
    print(hi)
    return




# t = 1
t = int(input())
import random
for i in range(t):
    solve(i)
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
