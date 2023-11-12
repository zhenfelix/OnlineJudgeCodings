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
    n, k = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        t, b = list(map(int, input().split()))
        arr.append((b,t))
    arr.sort(reverse=True)
    s = 0
    hq = []
    ans = 0
    for i in range(n):
        b, t = arr[i]
        s += t 
        heappush(hq,t)
        if i >= k:
            s -= heappop(hq)
        ans = max(ans,b*s)

    print(ans)
    
    return



# t = int(input())
t = 1
for _ in range(t):
    solve()
