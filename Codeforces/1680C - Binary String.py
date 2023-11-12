import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *
from math import *

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
    s = input()
    n = len(s)
    ps = [0]*(n+1)
    m = s.count('1')
    q1, q2 = deque(), deque()
    ans = m 
    for i in range(n):
        ch = s[i]
        if ch == '0': ps[i] += 1
        ps[i] += ps[i-1]
        ans = min(ans,max(ps[i],m-(i+1-ps[i])))
        if i-m >= 0:
            while q1 and -ps[q1[-1]] >= -ps[i-m]:
                q1.pop()
            q1.append(i-m)
        while q2 and q2[0] <= i-m:
            q2.popleft()
        if q2:
            j = q2[0]
            ans = min(ans,ps[i]-ps[j]-(i-j)+m)
        if q1:
            j = q1[0]
            ans = min(ans,ps[i]-ps[j])
        while q2 and -ps[q2[-1]]+q2[-1] >= -ps[i]+i:
            q2.pop()
        q2.append(i)
    print(ans)
    return 
def solve():
    s = input()
    n = len(s)
    m = s.count('1')
    zeros, ones = 0, m 
    ans = m 
    j = 0
    for i in range(n):
        if s[i] == '0': zeros += 1
        else: ones -= 1
        while j <= i and zeros > ones:
            if s[j] == '0': zeros -= 1
            else: ones += 1
            j += 1
        ans = min(ans, max(zeros,ones))
    print(ans)
    return 

t = int(input())
for _ in range(t):
    solve()
