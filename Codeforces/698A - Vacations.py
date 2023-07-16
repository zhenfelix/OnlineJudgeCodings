import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from math import *

n = int(input())
arr = list(map(int, input().split()))

@lru_cache(None)
def dfs(i,pre):
    if i == n:
        return 0
    res = inf 
    for cur in range(3):
        if cur > 0 and arr[i] == 0: continue
        if (cur == 0) or (pre != cur and ((arr[i]>>(cur-1))&1)):
            res = min(res, dfs(i+1,cur)+(cur==0)) 
    # print(i,pre,res)
    return res

print(dfs(0,0))