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
    n = int(input())
    xrr = list(map(int,input().split()))
    trr = list(map(int,input().split()))
    def check(mx):
        lo, hi = -inf, inf 
        for x, t in zip(xrr,trr):
            delta = mx-t
            lo = max(lo, x-delta)
            hi = min(hi, x+delta)
            if lo > hi:
                return inf
        return (lo+hi)/2 

    l, r = max(trr), max(trr)+max(xrr) 
    epsilon = 10**-6
    while r-l >= epsilon:
        mid = (l+r)/2
        if check(mid) == inf:
            l = mid 
        else:
            r = mid 
    print(check(r))

    return 


# t = 1
t = int(input())
import random
for i in range(t):
    solve()
