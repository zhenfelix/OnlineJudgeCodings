# import sys, heapq
# from collections import *
# from functools import lru_cache
# sys.setrecursionlimit(10**6)



# def main():

#     # sys.stdin = open('input.txt', 'r')
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         # arr = list(map(int, input().split(' ')))
#         if n < 4:
#             print(-1)
#             continue
#         res = []
#         for i in range(n//4):
#             res += [x+i*4 for x in [2,4,1,3]]
#         res += [i for i in range(n//4*4+1,n+1)]

#         if n%4 == 2:
#             res[-2], res[-3] = res[-3], res[-2]
#         elif n%4 == 3:
#             p = [-7,-2,-6,-1,-3,-4,-5]
#             tmp = list(map(lambda x: res[p[x]],range(7)))
#             res = res[:-7]+tmp
#         print(' '.join(map(str,res)))




# if __name__ == "__main__":
#     main()


import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():

    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n = int(input())
        # arr = list(map(int, input().split(' ')))
        if n < 4:
            print(-1)
            continue
        res = [i for i in range(1,n+1)[::-1] if i&1]
        res += [4,2]
        res += [i for i in range(6,n+1) if i&1==0]

        print(' '.join(map(str,res)))




if __name__ == "__main__":
    main()


