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
    intervals = []
    for _ in range(m):
        l, r = list(map(int,input().split()))
        intervals.append((l,r))
    poss = []
    q = int(input().strip())
    for _ in range(q):
        p = int(input().strip())
        poss.append(p)
    lo, hi = 0, q 
    while lo <= hi:
        psum = [0]*(n+1)
        mid = (lo+hi)//2
        for i in range(mid):
            psum[poss[i]] = 1
        for i in range(n):
            psum[i+1] += psum[i] 
        def check():
            for l, r in intervals:
                if (psum[r]-psum[l-1])*2 > r-l+1:
                    return True 
            return False
        if check():
            hi = mid - 1
        else:
            lo = mid + 1
    if lo > q:
        print(-1)
    else:
        print(lo)
            
    
        


# t = 1
t = int(input())
import random
for i in range(t):
    solve()
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
