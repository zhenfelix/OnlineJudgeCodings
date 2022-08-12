import sys, heapq
from collections import *
from functools import lru_cache



def main():

    def solve(arr):
        seen = set(arr)
        res = [arr[0]]
        for cur in arr:
            for i in range(33):
                tmp = [cur]
                if cur+(1<<i) in seen:
                    tmp.append(cur+(1<<i))
                if cur-(1<<i) in seen:
                    tmp.append(cur-(1<<i))
                if len(tmp) > len(res):
                    res = tmp 
                    if len(res) == 3:
                        break
        print(len(res))
        print(*res)
        return 

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    n = input()
    arr = list(map(int, input().split()))
    t = 1
    for _ in range(t):
        solve(arr)

    # debug(ans)


if __name__ == "__main__":
    main()


