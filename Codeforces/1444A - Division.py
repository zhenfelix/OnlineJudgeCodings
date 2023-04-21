import sys
# sys.stdin = open("contests/input","r")

from collections import *
# from math import *

def solve():
    p, q = list(map(int,input().split()))
    if p%q: return p 
    fs = Counter()
    f = 2
    while f*f <= q:
        while q%f == 0:
            fs[f] += 1
            q //= f 
        f += 1
    if q > 1:
        fs[q] += 1
    ans = 0
    for k, v in fs.items():
        cc = 0
        y = p 
        while y%k == 0:
            y //= k 
            cc += 1
        ans = max(ans,y*pow(k,v-1))
    return ans 

    # ans = 0
    # for k, v in fs.items():
    #     x = pow(k,v)
    #     y = p 
    #     while y%x == 0:
    #         y //= k 
    #     ans = max(ans,y)
    # return ans 
    


t = int(input())
for _ in range(t):
    print(solve())