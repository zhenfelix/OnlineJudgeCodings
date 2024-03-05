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
    # n = int(input())
    n, m = list(map(int,input().split()))
    reach = [-1]*n 
    for _ in range(m):
        a, b = list(map(int,input().split()))
        a -= 1
        b -= 1
        if a > b: a, b = b, a 
        reach[b] = max(reach[b], a) 
    ans = 0
    cur = -1
    for r in range(n):
        cur = max(cur,reach[r])
        ans += r-cur 
    print(ans)
    return 


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
