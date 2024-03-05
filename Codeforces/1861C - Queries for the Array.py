import sys,os

# sys.stdin = open("input","r") 

input = sys.stdin.readline


from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *
from math import *
from string import ascii_lowercase

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

MOD = 10**9+7
def solve():
    # t = int(input())
    s = input().strip()
    st = []
    for ch in s:
        if ch == '0':
            if len(st) >= 2 and (st[-1] == -1 or st[-1] == 0):
                if st[-1] == -1:
                    st[-1] = 0
            else:
                return False 
        elif ch == '1':
            if len(st) < 2 or (st[-1] == -1 or st[-1] == 1):
                if st and st[-1] == -1:
                    for i in range(len(st))[::-1]:
                        if st[i] != -1: break 
                        st[i] = 1
            else:
                return False
        elif ch == '+':
            if st and st[-1] == 0:
                st.append(0)  
            else:
                st.append(-1)
        else:
            st.pop()
        
    return True



t = int(input())
# t = 1
for _ in range(t):
    if solve():
        print("YES")
    else:
        print("NO")
