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

MOD = 10**9+7
def solve():
    n, k = list(map(int,input().split()))
    arr = []
    for _ in range(n):
        a = int(input())
        arr.append(a)
    cc = Counter()
    hq = []
    seen = set()
    ans = []
    for i, a in enumerate(arr):
        if cc[a] == 0:
            seen.add(a)
            heappush(hq,-a)
        elif cc[a] == 1:
            seen.remove(a)
        cc[a] += 1
        if i-k >= 0:
            a = arr[i-k]
            cc[a] -= 1
            if cc[a] == 1:
                seen.add(a)
                heappush(hq,-a)
            elif cc[a] == 0:
                seen.remove(a)
        if i >= k-1:
            while hq and -hq[0] not in seen:
                heappop(hq)
            if not hq:
                print("Nothing")
            else:
                print(-hq[0])


    return 


t = 1
# t = int(input())
import random
for i in range(t):
    solve()
