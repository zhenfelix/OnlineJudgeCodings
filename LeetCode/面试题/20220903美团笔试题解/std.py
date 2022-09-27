from collections import *
from functools import *
from heapq import * 
import sys 

sys.setrecursionlimit(10**7)

# 作者：王悟空
# 链接：https://www.nowcoder.com/discuss/1038729
# 来源：牛客网

def main():
    n, m, k = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
     
    h = [(0, i) for i in range(1, n + 1)]
    pre = [-1] * (n + 1)
    pre[k] = 0
    v1 = (0, k) # 最大
    v2 = (0, 0) # 次大
     
    for i in range(m):
        v = 0
        # 直通
        if pre[c[i]] != -1:
            v = max(v, pre[c[i]] + a[i])
     
        if c[i] != v1[1]:
            v = max(v, v1[0] + b[i])
        elif c[i] != v2[1]:
            v = max(v, v2[0] + b[i])
     
        pre[c[i]] = max(pre[c[i]], v)
     
        if v > v1[0]:
            if c[i] == v1[1]:
                v1 = (v, c[i])
            else:
                v1, v2 = (v, c[i]), v1
        elif v > v2[0]:
            v2 = (v, c[i])
     
    print(max(pre))

# 作者：王悟空
# 链接：https://www.nowcoder.com/discuss/1038729
# 来源：牛客网

# def main():
#     n, m, k = list(map(int, input().split()))
#     c = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
     
#     @lru_cache(None)
#     def f(i, k):
#         if i == m: return 0
#         if c[i] == k: return f(i+1, k) + a[i]
#         return max(
#             f(i + 1, k),
#             f(i + 1, c[i]) + b[i]
#         )
#     print(f(0, k))


if __name__ == '__main__':
    # sys.stdin = open('duipai/data.in', 'r')
    main()