import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *
from math import *
from string import ascii_lowercase

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
    cc = Counter(s)
    left, right = [], []
    flag = True 
    cnt = 0
    for ch in ascii_lowercase:
        v = cc[ch]
        if v == 0: continue
        if flag:
            left.append(ch*(v//2))
            right.append(ch*(v//2))
            if v%2:
                right.append(ch)
                flag = False
        else:
            left.append(ch*v)
            cnt += 1
    if cnt == 1:
        other = left.pop()
        ch = right.pop()
        left.append(other[::2])
        right.append(other[1::2])
        left.append(ch)
    print(''.join(left+right[::-1]))
        
    return 


t = int(input())
for _ in range(t):
    solve()
