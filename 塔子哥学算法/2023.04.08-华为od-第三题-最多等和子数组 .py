# 题目内容

# 给定一个数组,从中选出若干个不相交的子数组，满足各个子数组的和都相等.这样称为一次合法筛选。塔子哥现在想选出尽量多的子数组，求这个最多的个数。前提是满足合法筛选哦~
# 输入描述

# 第一行输入为数组长度 NN，1≤N≤10001≤N≤1000。

# 第二行为NN个用空格分开的整数 CiCi​，(−100000≤Ci≤100000)(−100000≤Ci​≤100000)。
# 输出描述

# 一行,一个整数 MM，表示满足要求的最多的组内子序列的数目。
# 样例

# 输入1

# 10
# 8 8 9 1 9 6 3 9 1 0

# 输出1

# 4

# 说明:

# 选出和为9的子数组,4个子数组分别为:[3,3],[5,5],[6,7],[8,8][3,3],[5,5],[6,7],[8,8] , 下标从11开始。

# 输入2

# 10
# -1 0 4 -3 6 5 -6 5 -7 -3

# 输出2

# 3

# 说明:

# 选出和为-3的子数组,3个子数组分别为:[4,4],[6,9],[10,10][4,4],[6,9],[10,10] , 下标从11开始。


from collections import *
n = int(input())
arr = list(map(int,input().split()))
mp = defaultdict(list)
for i in range(n):
    s = 0
    for j in range(i,n):
        s += arr[j]
        mp[s].append((i,j))
ans = 0
for _, vs in mp.items():
    vs.sort(key = lambda x: x[-1])
    # print(vs)
    cnt = 0
    cur = -1
    for i, j in vs:
        if i > cur:
            cnt += 1
            cur = j 
    ans = max(ans, cnt)
print(ans)