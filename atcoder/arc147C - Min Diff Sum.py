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
    L, R = [0]*n, [0]*n 
    for i in range(n):
        l, r = list(map(int,input().split()))
        L[i] = l 
        R[i] = r 
    L.sort(reverse=True)
    R.sort()
    ans = 0
    for i in range(n):
        l, r = L[i], R[i]
        if l <= r: break
        ans += (n-1-i*2)*(l-r)
    print(ans)
    return 


# t = int(input())
t = 1
for _ in range(t):
    solve()
