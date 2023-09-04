import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from math import *

t = int(input())
for _ in range(t):
    n, m = list(map(int,input().split()))
    s = input()
    s = list(map(int,s))
    tot = n*m 
    ans = [0]*tot 
    cols = [0]*tot 
    for i in range(tot):
        pre = cols[i-m] if i-m >= 0 else 0 
        cols[i] = pre|s[i]
    # print(cols)
    cnt = 0
    for i in range(tot):
        cnt += cols[i]
        if i-m >= 0:
            cnt -= cols[i-m]   
        ans[i] += cnt 
    # print(ans)
    rows = [0]*(tot+1)
    for i in range(tot):
        rows[i] = s[i]+rows[i-1]
    for i in range(tot)[::-1]:
        if i-m >= 0:
            rows[i] -= rows[i-m]
    # print(rows)
    for i in range(tot):
        rows[i] = 1 if rows[i] else 0
        if i-m >= 0:
            rows[i] += rows[i-m]
        ans[i] += rows[i]
    # print(rows)
    print(*ans)

