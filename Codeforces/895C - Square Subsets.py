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
    arr = list(map(int,input().split()))
    nmax = 71
    ps = [1]*nmax
    fs = []
    for f in range(2,nmax):
        if ps[f] == 0: continue
        fs.append(f)
        for k in range(f*f,nmax,f):
            ps[k] = 0
    # print(fs,len(fs))
    m = len(fs)
    cc = Counter(arr)
    dp = [0]*(2**m)
    dp[0] = 1
    pows = [1]*(n+1)
    for i in range(n):
        pows[i+1] = (pows[i]*2)%MOD
    for a in range(1,nmax):
        c = cc[a]
        if c == 0: continue
        ndp = [0]*(2**m)
        mask = 0
        for i, f in enumerate(fs):
            while a%f == 0:
                mask ^= (1<<i)
                a //= f 
        for s in range(2**m):
            ndp[s] = (ndp[s]+dp[s]*pows[c-1])%MOD
            ndp[s^mask] = (ndp[s^mask]+dp[s]*pows[c-1])%MOD
        dp = ndp
    print((dp[0]-1)%MOD)
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
