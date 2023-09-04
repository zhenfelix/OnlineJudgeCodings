import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from math import *

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    i = 0
    ans = 0
    arr = []
    while i < n:
        if s[i:i+5] == "twone":
            ans += 1
            arr.append(i+2+1)
            i += 5
        elif s[i:i+3] in ["two","one"]:
            ans += 1
            arr.append(i+1+1)
            i += 3
        else:
            i += 1
    print(ans)
    print(*arr)