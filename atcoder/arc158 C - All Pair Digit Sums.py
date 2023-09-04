import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from math import *

n = int(input())
arr = list(map(int,input().split()))
m = 15
ans = sum(sum(map(int,list(str(a)))) for a in arr)*n*2
# print(ans)
base = 10
for _ in range(m):
    brr = sorted([a%base for a in arr])
    # print(brr)
    # if brr[-1]*2 < base:
    #     break 
    j = n-1
    for i in range(n):
        while j >= 0 and brr[i]+brr[j] >= base:
            j -= 1
        ans -= (n-1-j)*9
    base *= 10
print(ans)