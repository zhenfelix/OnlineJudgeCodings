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
    arr = list(map(int,input().split()))
    ans = 0
    cc = Counter(arr)
    candidates = []
    for a in range(1,n+1)[::-1]:
        if cc[a] == 0: candidates.append(a)
    visited = [0]*(n+1)
    for i, a in enumerate(arr):
        if candidates and (visited[a] or (cc[a] > 1 and a > candidates[-1])):
            cc[a] -= 1
            arr[i] = candidates.pop()
            ans += 1 
        visited[arr[i]] = 1
    print(ans)
    print(*arr)
    return 


# t = int(input())
t = 1
for _ in range(t):
    solve()
