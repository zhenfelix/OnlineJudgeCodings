import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
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

n = int(input())
arr = list(map(int,input().split()))

ans = sum(l//2*(n-l+1) for l in range(1,n+1))
mp = defaultdict(list)
for i, a in enumerate(arr):
    mp[a].append(i)
for _, brr in mp.items():
    m = len(brr)
    l, r = 0, m-1
    while l < r:
        if brr[l]+brr[r] < n:
            ans -= (brr[l]+1)*(r-l)
            l += 1
        else:
            ans -= (n-brr[r])*(r-l)
            r -= 1

print(ans)