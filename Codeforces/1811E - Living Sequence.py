import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from math import *

t = int(input())
for _ in range(t):
    x = int(input())
    y = 0
    base = 1
    while x:
        r = x%9
        y += (r+1 if r >= 4 else r)*base
        base *= 10
        x //= 9 
    print(y)
