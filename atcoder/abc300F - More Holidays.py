import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
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

n, m, k = list(map(int,input().split()))
# arr = list(map(int,input().split()))
# n = int(input())
# L, N1, N2 = list(map(int,input().split()))
s = input()

def solve():
    global s, n 
    cc = s.count('x')
    if cc*m == k:
        return n*m 
    cur = k//cc*n 
    if k//cc < m-1:
        s = s+s 
        n += n 
    
    ans, j, cnt = 0, 0, k//cc*cc 
    for i in range(n):
        if s[i] == 'x': cnt += 1
        cur += 1
        while cnt > k and j < n:
            if s[j] == 'x':
                cnt -= 1
            cur -= 1
            j += 1
        ans = max(ans,cur) 

    return ans 

print(solve())