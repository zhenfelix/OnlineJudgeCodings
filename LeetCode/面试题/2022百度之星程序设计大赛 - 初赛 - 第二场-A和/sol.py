from collections import *
from functools import *
from heapq import * 
import sys 



def solve():
    n,q,k,x = map(int,input().split())
    arr = list(map(int,input().split()))
    hq2, hq = [], []
    state = [0]*n 
    reach = [float('inf')]*n 
    j = -1
    s = 0
    cnt = 0
    for i in range(n):
        if i > 0 and state[i-1] == 1:
            state[i-1] = 0
        if i > 0 and state[i-1] == 2:
            cnt -= 1
            state[i-1] = 0 
            s -= arr[i-1]
            while hq:
                if cnt >= k:
                    break 
                w, r = heappop(hq)
                if state[r] == 1:
                    cnt += 1
                    state[r] = 2
                    s -= w 
                    heappush(hq2,(-w,r))
        while j+1 < n and s < x:
            j += 1
            state[j] = 2
            cnt += 1
            heappush(hq2, (arr[j],j))
            s += arr[j]
            while cnt > k or (state[hq2[0][1]] != 2):
                w, r = heappop(hq2)
                if state[r] == 2:
                    cnt -= 1
                    state[r] = 1
                    s -= w 
                    heappush(hq,(-w,r))
        if s >= x:
            reach[i] = j 
        # print(i,s,cnt,reach[i],j,[ii for ii in range(j+1) if state[ii]==2],[ii for ii in range(j+1) if state[ii]==1])
    for i in range(q):
        l, r = list(map(int,input().split()))
        l -= 1
        r -= 1
        if r < reach[l]:
            print("N")
        else:
            print("Y")


# sys.stdin = open('duipai/data.in', 'r')
# print(solve())
solve()