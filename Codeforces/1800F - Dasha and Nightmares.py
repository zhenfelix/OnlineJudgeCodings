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
    # arr = list(map(int,input().split()))
    xs, ys = [], []
    for i in range(n):
        s = input().strip()
        x, y = 0, 0
        for ch in s:
            idx = ord(ch)-ord('a')
            x ^= (1<<idx)
            y |= (1<<idx)  
        xs.append(x)
        ys.append(y)
    
    ans = 0
    mask = (1<<26)-1
    for idx in range(26):
        cc = Counter()
        for i in range(n):
            if ys[i]&(1<<idx) == 0:
                ans += cc[mask^(1<<idx)^xs[i]]
                cc[xs[i]] += 1
    print(ans)

    return 


t = 1
# t = int(input())
import random
for i in range(t):
    solve()
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
