
# 2022年9月23日-华为秋招机考-第三题-最省出游方案

# 小明规划寒假出游nn个城市，nn个城市间的直达交通费由一个二维矩阵表示。求小明从城市0出发，游遍其余n−1n−1个城市后重新回到城市00的最低花费是多少。假设至少存在这样的一条游玩线路，且同一城市可以多次经过。
# 输入描述

# 第一行一个整数nn(1≤n≤151≤n≤15)

# 接下来nn行,每行nn个整数。代表邻接矩阵, (1≤ai,j≤1000)(1≤ai,j​≤1000) , ai,i=0ai,i​=0
# 输出描述

# 输出一个整数,代表最低花费
# 样例1

# 输入

# 4
# 0 3 1 2
# 4 0 2 1
# 4 1 0 1
# 2 1 4 0

# 输出

# 5


from math import * 
from heapq import *
n = int(input())
dist = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    dist.append(tmp)
dp = [[inf]*n for _ in range(1<<n)]
dp[1][0] = 0
for s in range(1,1<<n):
    hq = [(dp[s][i],i) for i in range(n)]
    while hq:
        d, i = heappop(hq)
        if d > dp[s][i] or (s&(1<<i) == 0): continue
        for j in range(n):
            ns = s|(1<<j)
            if d+dist[i][j] < dp[ns][j]:
                dp[ns][j] = d+dist[i][j]
                heappush(hq,(dp[ns][j],j))
print(dp[-1][0])