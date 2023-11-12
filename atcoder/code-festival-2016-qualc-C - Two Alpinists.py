import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
from math import *

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
brr = list(map(int,input().split()))
crr = list(map(int,input().split()))

# n = int(input())
# L, N1, N2 = list(map(int,input().split()))
MOD = 10**9+7
def solve():
    lo, hi = [brr[0]]*n, [brr[0]]*n 
    ans = 1
    for i in range(1,n):
        if brr[i] < brr[i-1]:
            return 0 
        else:
            lo[i] = hi[i] = brr[i]
            if brr[i] == brr[i-1]:
                lo[i] = 1
    if crr[-1] > hi[-1] or crr[-1] < lo[-1]:
        return 0
    for i in range(n-1)[::-1]:
        if crr[i] < crr[i+1]:
            return 0 
        elif crr[i] == crr[i+1]:
            l = r = crr[i]
            if crr[i] == crr[i+1]:
                l = 1
            l = max(l,lo[i])
            r = min(r,hi[i])
            if l > r: return 0 
            ans = (ans*(r-l+1))%MOD 
    return ans 



print(solve())