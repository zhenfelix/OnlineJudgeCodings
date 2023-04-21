# 题目内容

# 塔子哥最近喜欢和朋友一起玩弹珠，他现在想研究一下弹珠的行走轨迹，以此来提高自己和朋友一起玩弹珠的时候的胜率。

# 当弹珠撞到墙的时候会发生反弹，方向发生改变，参考下图：

# image

# 弹珠将不断行进，永不停止。

# 现在给定了桌面大小，以及弹珠的初始坐标和初始方向。请问小球多少秒后将回到初始点？
# 输入描述

# 第一行输入两个正整数 nn 和 mm ，代表桌面矩阵的行数和列数。

# 第二行输入两个正整数 ii 和 jj 以及一一个长度为 22 的字符串 dd 代表弹珠的初始坐标和方向。

# 1≤n,m≤20001≤n,m≤2000

# 1≤i≤n1≤i≤n

# 1≤j≤m1≤j≤m

# d∈{DR,DL,UR,UL}d∈{DR,DL,UR,UL}
# 输出描述

# 一个整数，代表弹珠回到初始点需要经过的秒数。
# 样例

# 输入

# 5 5
# 1 1 DR

# 输出

# 8

from math import *
n,m=list(map(int,input().split()))
x,y,s=input().split()
n -= 1
m -= 1
x = int(x)-1
y = int(y)-1
dirs = ["DR","DL","UR","UL"]
mp = {ch:i for i, ch in enumerate(dirs)}
dxy = [[1,1],[1,-1],[-1,1],[-1,-1]]
dx, dy = dxy[mp[s]]
cnt = 0
cx, cy = x, y
while True:
    cnt += 1
    if cx+dx > n or cx+dx < 0:
        dx = -dx 
    cx += dx 
    if cy+dy > m or cy+dy < 0:
        dy = -dy 
    cy += dy 
    if (cx,cy) == (x,y):
        break 
print(cnt)