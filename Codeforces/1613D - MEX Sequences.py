import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from math import *

MOD = 998244353
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cc = [0]*(n+10)
    cc[-1] += 1
    cc1 = [0]*(n+10)
    ans = 0
    for a in arr:
        # print(a,cc,cc1,cc[a]+cc[a-1]+cc[a-2]+cc1[a]*2)
        ans += cc[a]+cc[a-1]+cc[a-2]+cc1[a]+cc1[a+2]
        ans %= MOD 
        cc[a] += cc[a]+cc[a-1]
        cc[a] %= MOD
        cc1[a+2] += cc1[a+2]
        cc1[a+2] %= MOD
        cc1[a] += cc1[a]+cc[a-2]
        cc1[a] %= MOD
    print(ans)

