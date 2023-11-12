import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
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

MOD = 10**9+7
def solve():
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    ans = 0
    brr = []
    for a in arr:
        ans += a//k
        brr.append(a%k)
    brr.sort()
    i, j = 0, n-1
    while i < j:
        if brr[i] + brr[j] < k:
            i += 1
        else:
            i += 1
            j -= 1
            ans += 1
    print(ans)
    return 


t = int(input())
for _ in range(t):
    solve()
