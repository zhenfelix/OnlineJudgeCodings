# # https://www.luogu.com.cn/problem/T130108?contestId=27163
# # https://www.luogu.com.cn/blog/12cow/SBCOI2020

# import sys, heapq
# from collections import *
# from functools import lru_cache
# sys.setrecursionlimit(10**6)


# @lru_cache(None)
# def dfs(lo,hi):
#     if lo >= hi:
#         return 0
#     return min(max(dfs(lo,i),dfs(i+1,hi))+cost[i] for i in range(lo,hi))



# # sys.stdin = open('input.txt', 'r')
# t = input()
# t = int(t)
# for _ in range(t):
#     n = input()
#     n = int(n)
#     cost = list(map(int, input().split(' ')))
#     cost= [0] + cost
#     print(dfs(1,n))
#     dfs.clear()

# https://www.luogu.com.cn/problem/T130108?contestId=27163
# https://www.luogu.com.cn/blog/12cow/SBCOI2020

import sys, heapq
from collections import *
from functools import lru_cache
# sys.setrecursionlimit(10**6)



def main():

    # @lru_cache(None)
    # def dfs(lo, hi):
    #     if lo >= hi:
    #         return 0
    #     return min(max(dfs(lo, i), dfs(i + 1, hi)) + cost[i] for i in range(lo, hi))

    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n = int(input())
        cost = list(map(int, input().split(' ')))
        cost = [0] + cost
        dp = defaultdict(int)
        for j in range(1,n+1):
            k = j-1
            # q = deque()
            q = [0]*n
            left, right = n, n-1
            for i in range(1,j)[::-1]:
                while k >= i and dp[i,k] >= dp[k+1,j]:
                    k -= 1
                k += 1
                while right >= left and q[right] >= k:
                    right -= 1
                    # q.pop()
                if i < k:
                    while right >= left and dp[q[left]+1,j]+cost[q[left]] >= dp[i+1,j]+cost[i]:
                        left += 1
                        # q.popleft()
                    left -= 1
                    q[left] = i
                    # q.appendleft(i)
                dp[i,j] = dp[i,k]+cost[k]
                if right >= left:
                    dp[i,j] = min(dp[i,j],dp[q[right]+1,j]+cost[q[right]])
                # print(i,j,dp[i,j],k)
        # print(dp)
        print(dp[1,n])


if __name__ == "__main__":
    main()
