
# 2023.04.08-美团春招-第四题-田地行走
# 题目描述：

# 塔子哥是一个农民，他有一片 n×mn×m 大小的田地，共 nn 行 mm 列，其中行和列都用从 11 开始的整数编号，田地中有 kk 个格子中埋有土豆。我们记第 aa 行第 bb 列的格子为 (a,b)(a,b) 。塔子哥现在位于 (x1,y1)(x1,y1) ，他想要移动到 (x2,y2)(x2,y2) 处去收菜，但是他不想阻碍自己土地里土豆的生长情况，所以他不想在移动过程中碰到土豆。

# 塔子哥每次移动可以移动到与他所处格子的相邻的一格中，形式化地说，如果塔子哥位于 (x,y)(x,y) ，则塔子哥可以移动到 (x−1,y)(x−1,y) ， (x+1,y)(x+1,y) ， (x,y−1)(x,y−1) ， (x,y+1)(x,y+1) 的格子之一，但塔子哥不能移动到田地之外。

# 塔子哥想要在移动过程中，离这些土豆越远越好，而不是走最短路径。

# 这里定义两个格子之间的距离为曼哈顿距离，即格子 (a,b)(a,b) 和 (c,d)(c,d) 之间的距离是 ∣a−c∣+∣b−d∣∣a−c∣+∣b−d∣ 。

# 塔子哥想知道，移动中与土豆之间距离的最小值最大可能是多少。

# 请注意，如果无论塔子哥如何移动，都会进入一个有土豆的格子的话，这个最大可能值为 00 。
# 输入描述

# 第一行三个整数 nn， mm ， kk ，分别表示田地的行数，列数和土豆个数。

# 接下来 kk 行，每行两个整数 pp ， qq ，表示一个土豆放置在格子 (p,q)(p,q) 中。任意两土豆的放置位置不同。

# 接下来一行四个整数 x1x1 ， y1y1， x2x2 ， y2y2 ，表示塔子哥的出发位置和目的位置。保证塔子哥的出发位置和目的位置上没有土豆。

# 对于全部数据，

# 1≤n,m≤5001≤n,m≤500 ，

# n×m≥3n×m≥3，

# 1≤k≤min{n×m−2,400}1≤k≤min{n×m−2,400} ，

# 1≤p,x1,x2≤n1≤p,x1,x2≤n ，

# 1≤q,y1,y2≤m,(x1,y1)≠(x2,y2)1≤q,y1,y2≤m,(x1,y1)=(x2,y2) ，

# 保证 (x1,y1)(x1,y1) 和 (x2,y2)(x2,y2) 中没有土豆，并且一个格子中最多放置一个土豆。
# 输出描述

# 输出一行一个整数，表示移动过程中与土豆之间距离的最小值的可能最大值。
# 样例

# 输入

# 5 6 2
# 2 1
# 2 3
# 1 1 5 1

# 输出

# 1


from math import *
from collections import * 

n,m,k = list(map(int,input().split()))
potato = []
for _ in range(k):
    p, q = list(map(int,input().split()))
    p -= 1
    q -= 1
    potato.append((p,q))
x1,y1,x2,y2 = list(map(int,input().split()))
x1-=1
y1-=1
x2-=1
y2-=1
dist = [[inf]*m for _ in range(n)]
for p,q in potato:
    dist[p][q] = 0
dxy = [-1,0,1,0,-1]
while potato:
    tmp = []
    for p,q in potato:
        for dx,dy in zip(dxy[:-1],dxy[1:]):
            dx += p 
            dy += q 
            if 0 <= dx < n and 0 <= dy < m and dist[dx][dy] > dist[p][q]+1:
                dist[dx][dy] = dist[p][q]+1
                tmp.append((dx,dy))
    potato = tmp 

def bfs(limit):
    if dist[x1][y1] < limit:
        return False
    myq = deque([(x1,y1)])
    visited = set()
    visited.add((x1,y1))
    while myq:
        x,y = myq.popleft()
        if (x,y) == (x2,y2):
            return True
        for dx,dy in zip(dxy[:-1],dxy[1:]):
            dx += x 
            dy += y 
            if 0 <= dx < n and 0 <= dy < m and (dx,dy) not in visited and dist[dx][dy] >= limit:
                myq.append((dx,dy))
                visited.add((dx,dy))
    return False 

lo, hi = 0, n+m 
while lo <= hi:
    mid = (lo+hi)//2
    if bfs(mid):
        lo = mid+1
    else:
        hi = mid-1
print(hi)

