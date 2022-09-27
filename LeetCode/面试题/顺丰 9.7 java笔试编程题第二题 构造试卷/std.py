from collections import *
from functools import *
from heapq import * 
import sys 

sys.setrecursionlimit(10**7)


def main():
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    cnt = 0
    pq = [-a for a in arr]
    heapify(pq)
    while len(pq) >= m:
        tmp = []
        for _ in range(m):
            a = heappop(pq)
            if a+1 < 0:
                tmp.append(a+1)
        for a in tmp:
            heappush(pq,a)
        # print(sorted(pq))
        cnt += 1
    print(cnt)
    return


    
     



if __name__ == '__main__':
    # sys.stdin = open('duipai/data.in', 'r')
    main()