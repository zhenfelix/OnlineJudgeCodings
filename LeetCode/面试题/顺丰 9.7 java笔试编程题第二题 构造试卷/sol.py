from collections import *
from functools import *
from heapq import * 
import sys 
from bisect import * 



# def solve():
#     n, m = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#     arr.sort()
#     s = arr.copy()
#     for i in range(1,n):
#         s[i] += s[i-1]
    
#     lo, hi = 1, s[-1]
#     s.append(0)
#     # arr.append(float('inf'))
#     while lo <= hi:
#         k = (lo+hi)//2
#         cnt = bisect_left(arr, k)
#         if s[cnt-1]//k+n-cnt >= m:
#             lo = k + 1
#         else:
#             hi = k - 1
#     print(hi)
#     return  


# def solve():
#     n, m = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#     arr.sort()
#     s = arr.copy()
#     for i in range(1,n):
#         s[i] += s[i-1]
    
#     # arr.append(float('inf'))
#     ans = 0
#     for i in range(n):
#         if m <= n-i-1:
#             continue
#         if s[i]//(m-(n-i-1)) >= arr[i]:
#             ans = s[i]//(m-(n-i-1))
#     print(ans)
#     return  


def solve():
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    s = arr.copy()
    for i in range(1,n):
        s[i] += s[i-1]
    
    # arr.append(float('inf'))
    lo, hi = 0, n-1
    while lo <= hi:
        i = (lo+hi)//2
        if m <= n-i-1 or s[i]//(m-(n-i-1)) >= arr[i]:
            lo = i + 1
        else:
            hi = i - 1
    print(s[hi]//(m-(n-hi-1)))
    return  

# sys.stdin = open('duipai/data.in', 'r')
# print(solve())
solve()