import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from math import *

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))


tot = sum(arr)
cur, cnt = 0, 0
hq = [-b for b in brr]
heapify(hq)
while hq:
    if cur >= tot: break
    cnt += 1
    cur -= heappop(hq)

volumn = sum(brr)
mx = 0
dp = [[-inf]*(volumn+1) for _ in range(cnt+1)]
dp[0][0] = 0
for a, b in zip(arr,brr):
    for j in range(1,cnt+1)[::-1]:
        for k in range(b,volumn+1)[::-1]:
            dp[j][k] = max(dp[j][k],dp[j-1][k-b]+a)

print(cnt,tot-max(dp[cnt][a] for a in range(tot,volumn+1)))


