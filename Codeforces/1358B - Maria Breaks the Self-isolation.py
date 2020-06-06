import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():




    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        # n, m = map(int,input().split(' '))
        n = int(input())
        arr = list(map(int,input().split(' ')))
        cnt = Counter(arr)
        presum, tmp = 0, 0
        for i in sorted(cnt):
            tmp += cnt[i]
            if presum+tmp >= i:
                presum += tmp
                tmp = 0
            # print(i,cnt,presum,tmp)
        print(presum+1)







if __name__ == "__main__":
    main()




