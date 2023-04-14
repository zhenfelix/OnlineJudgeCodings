
# 2023.4.2-网易有道研发岗-第四题-机器采草莓最优决策
# 题目内容

# 采草莓机器人在一个n∗mn∗m的草莓矩阵内，从起点坐标(0，0)(0，0)出发，可以向右或向下两个方向移动，每个方格种植着不同价值的草莓，现在塔子哥规定了一个阈值gg,代表该机器人此行采集草莓的总价值的最低目标值，塔子哥想知道机器人计算完成任务所需要移动的最少移动次数可以满足这个阈值？
# 输入描述

# 第一行输入三个整数:n,m,gn,m,g , 以空格隔开。

# 接下来有nn行，每行有mm个整数，以空格隔开。这n∗mn∗m 个数字构成草莓矩阵.

# 数据范围:

# 1≤n,m≤1000,1≤ai≤500,1≤g≤10000001≤n,m≤1000,1≤ai​≤500,1≤g≤1000000
# 输出描述

# 机器人完成任务所需移动的最少次数，不存在则返回-1
# 示例1

# 输入

# 1 1 8
# 10

# 输出

# 0

# 说明

# 机器人起点位置即可完成任务，不需要移动

# 示例2

# 输入

# 2 2 5
# 2 2
# 2 2

# 2

# 说明

# 需要向右移动一次，再向下移动一次

# 注意

# python用户建议使用pypy3提交


from math import *
n,m,g = list(map(int,input().split()))
arr = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    arr.append(tmp)
ans = inf 
for i in range(n):
    for j in range(m):
        pre = 0
        if i: pre = max(pre,arr[i-1][j])
        if j: pre = max(pre,arr[i][j-1])
        arr[i][j] += pre  
        if arr[i][j] >= g: ans = min(ans,i+j)
print(ans if ans < inf else -1)