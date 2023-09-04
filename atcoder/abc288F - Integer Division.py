import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from math import *

n = int(input())
arr = list(map(int,list(input())))
MOD = 998244353
ans = 0
pre = 0
s = 1
for a in arr:
    cur = 10*pre+a*s 
    cur %= MOD 
    s = (s+cur)%MOD 
    pre = cur 
print(cur)
