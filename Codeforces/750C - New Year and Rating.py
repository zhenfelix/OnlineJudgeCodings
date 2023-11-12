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
    n = int(input())
    arr = []
    lo, hi = -inf, inf 
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    for c, d in arr:
        if d == 1:
            lo = max(lo,1900)
        else:
            hi = min(hi,1899)
        lo += c 
        hi += c 
        if lo > hi: 
            print("Impossible")
            return
    if hi == inf:
        print("Infinity")
        return
    print(hi)
    return 


# t = int(input())
t = 1
for _ in range(t):
    solve()
