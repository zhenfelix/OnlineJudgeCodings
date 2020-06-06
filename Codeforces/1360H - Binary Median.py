import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():




    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n, m = map(int,input().split(' '))
        total = 2**m
        mid = (total-1)//2
        removes = set()
        for _ in range(n):
            s = input()
            cur = 0
            for ch in s:
                cur = cur<<1
                if ch == '1':
                    cur += 1
            removes.add(cur)
        removed = set()
        for r in removes:
            if total & 1 and r >= mid:
                while mid-1 in removed:
                    mid -= 1
                mid -= 1
            elif total & 1 == 0 and r <= mid:
                while mid+1 in removed:
                    mid += 1
                mid += 1
            total -= 1
            removed.add(r)
        res = []
        for i in range(m):
            if mid & (1<<i):
                res.append('1')
            else:
                res.append('0')
        # print(''.join(res[::-1]),mid)
        print(''.join(res[::-1]))






if __name__ == "__main__":
    main()




# import sys, heapq
# from collections import *
# from functools import lru_cache
# sys.setrecursionlimit(10**6)
# import bisect


# def main():




#     # sys.stdin = open('input.txt', 'r')
#     t = int(input())
#     for _ in range(t):
#         n, m = map(int,input().split(' '))
#         total = 2**m
#         target = (total-n-1)//2
#         removes = []
#         for _ in range(n):
#             s = input()
#             cur = 0
#             for ch in s:
#                 cur = cur<<1
#                 if ch == '1':
#                     cur += 1
#             removes.append(cur)
#         removes.sort()
#         lo, hi = 0, 2**m-1
#         while lo <= hi:
#             mid = (lo+hi)//2
#             i = bisect.bisect_left(removes,mid)
#             if mid-i <= target:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#         res = []
#         for i in range(m):
#             if hi & (1<<i):
#                 res.append('1')
#             else:
#                 res.append('0')
#         # print(''.join(res[::-1]),mid)
#         print(''.join(res[::-1]))






# if __name__ == "__main__":
#     main()



