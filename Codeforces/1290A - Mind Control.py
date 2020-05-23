import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():

    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split(' '))
        arr = list(map(int, input().split(' ')))
        # res = max(min(max(arr[i+j],arr[i+j+n-m]) for j in range(m-min(k,m-1))) for i in range(min(k+1,m)))
        # print(res)
        q = deque()
        k = min(k,m-1)
        res = -float('inf')
        for i in range(m):
            cur = max(arr[i],arr[i+n-m])
            while q and i - q[0][1] > m - 1 - k: q.popleft()
            while q and q[-1][0] > cur: q.pop()
            q.append((cur,i))
            if i >= m-1-k: res = max(res,q[0][0])
        print(res)


if __name__ == "__main__":
    main()


