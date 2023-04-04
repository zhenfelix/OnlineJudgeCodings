from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *
from string import *

ascii_lowercase = "ab"

def solve(n,arr):
    cc = Counter(arr)
    mx = max(arr)
    ans = [arr[0]]
    for a in arr:
        b = 1
        while a+b <= mx:
            if cc[a+b] and cc[a-b]:
                return [a-b,a,a+b]
            if cc[a+b]:
                ans = [a,a+b]
            b *= 2
    return ans 

    
def genseq(n,i,path,s,e,flo,fhi):
    if i == n: 
        yield path
        return
    lo = s[i] if flo else ascii_lowercase[0]
    hi = e[i] if fhi else ascii_lowercase[-1]
    for ch in ascii_lowercase:
        if lo <= ch <= hi:
            yield from genseq(n,i+1,path+ch,s,e,flo and ch == lo, fhi and ch == hi)
    return

def brute(n,s1,s2,evil):
    g = genseq(n,0,'',s1,s2,True,True)
    cnt = 0
    for s in g:
        if evil in s: 
            # print(s)
            continue
        cnt += 1
    return cnt 

def generate():
    
    n = randint(1,10)
    m = randint(1,n)
    s1 = ''.join(choices(ascii_lowercase,k=n))
    s2 = ''.join(choices(ascii_lowercase,k=n))
    if s1 > s2: s1, s2 = s2, s1 
    evil = ''.join(choices(ascii_lowercase,k=m))
    return n,s1,s2,evil




def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for i in range(1):
        # n, k = list(map(int,input().split()))
        n = int(input())
        arr = list(map(int,input().split()))
        # s = input()
        ans = solve(n,arr)        
        print(len(ans))
        print(*ans)
        # ans1 = solve(n,arr)

        # ans2 = brute(n,s1,s2,evil)
        # assert(ans1 == ans2)
        # print(f"{i}th test case ok")
        

if __name__ == "__main__":
    main()