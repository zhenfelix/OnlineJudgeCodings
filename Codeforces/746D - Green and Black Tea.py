import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from math import *

MOD = 998244353
n,k,a,b = list(map(int,input().split()))
A, B = 'G', 'B'
if a > b:
    a, b = b, a 
    A, B = B, A 
m = max((a+k-1)//k,(b+k-1)//k-1)
if m > a:
    print("NO")
else:
    ans = []
    ra, rb = a, b
    for i in range(m):
        r = m-i 
        pb = min(k,rb-r)
        ans.append(B*pb)
        rb -= pb
        pa = min(k,ra-r+1)
        ans.append(A*pa)
        ra -= pa 
    ans.append(B*rb)
    print(''.join(ans))

