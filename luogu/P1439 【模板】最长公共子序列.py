import sys, heapq
from collections import *
from functools import lru_cache
import bisect


def main():

    # sys.stdin = open('input.txt', 'r')
    # t = int(input())
    # for _ in range(t):
    #     n, m = map(int,input().split(' '))
    #
    n = int(input())
    p1 = list(map(int,input().split(' ')))
    p2 = list(map(int,input().split(' ')))
    idx = {}
    for i, x in enumerate(p1):
        idx[x] = i
    st = []
    for x in p2:
        i = bisect.bisect_left(st,idx[x])
        if i == len(st):
            st.append(idx[x])
        else:
            st[i] = idx[x]
    print(len(st))






if __name__ == "__main__":
    main()
