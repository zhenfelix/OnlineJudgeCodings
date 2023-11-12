import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
from math import *
from itertools import *

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

n = int(input())
# n, m = list(map(int,input().split()))
# arr = []
# for _ in range(n):
#     arr.append(list(map(int,input().split())))
arr = list(map(int,input().split()))
# crr = list(map(int,input().split()))

# n = int(input())
# L, N1, N2 = list(map(int,input().split()))
MOD = 10**9+7
def solve():
    arr.sort()
    neg = [a for a in arr if a < 0]
    pos = [a for a in arr if a > 0]
    candidates = []
    for brr in [neg,pos]:
        if len(brr) <= 6:
            candidates.extend(brr)
        else:
            candidates.extend(brr[:3])
            candidates.extend(brr[-3:])
    mx, mi = -inf, inf 
    for a, b, c in combinations(candidates,3):
        v = (a+b+c)/(a*b*c)
        mx = max(mx,v)
        mi = min(mi,v)
    print(mi)
    print(mx)

# print(solve())
solve()