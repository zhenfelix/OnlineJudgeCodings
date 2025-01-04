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
def solve():
    n, m = list(map(int,input().split()))
    g = defaultdict(list)
    for _ in range(m):
        x, y, w = list(map(int,input().split()))
        g[x].append((y,w*2))
        g[y].append((x,w*2))
    arr = list(map(int,input().split()))
    for i in range(n):
        g[0].append((i+1,arr[i]))
        g[i+1].append((0,arr[i]))
    dist = [inf]*(n+1)
    dist[0] = 0
    hq = [(0,0)]
    while hq:
        d, cur = heappop(hq)
        if d > dist[cur]: continue
        for nxt, w in g[cur]:
            if d+w < dist[nxt]:
                dist[nxt] = d+w 
                heappush(hq,(dist[nxt],nxt))
    print(*dist[1:])
    
        


t = 1
# t = int(input())
import random
for i in range(t):
    solve()
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
