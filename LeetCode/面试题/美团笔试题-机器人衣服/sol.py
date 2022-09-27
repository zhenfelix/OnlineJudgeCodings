from collections import *
from functools import *
from heapq import * 

def solve():
    n, B = list(map(int,input().split()))
    ts = list(map(int,input().split()))
    ps = list(map(int,input().split()))
    ps.append(0)

    def check(t):
        # if ps[0] > B:
        #     return False 
        dist = [float('inf')]*(n+1)
        q = [(ps[0],0)]
        dist[0] = ps[0]
        while q:
            w, i = heappop(q)
            if w > B:
                return False
            if i == n:
                return True
            if w > dist[i]:
                continue
            for j in range(i+1,n+1):
                if (j-i)*ts[i] > t:
                    break
                if w+ps[j] < dist[j]:
                    dist[j] = w+ps[j]
                    heappush(q,(dist[j],j))
        return False


    mx = max(ts)*n 
    lo, hi = 1, mx 
    while lo <= hi:
        mid = (lo+hi)//2
        if check(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    ans = lo 
    
    return ans if ans <= mx else -1
    # return -1


print(solve())