
# 2023.04.13-华为实习笔试-第二题-获取最多食物
# 题目内容

# 塔子哥设计的这个游戏是一个冒险类游戏，参与者需要在地图上寻找食物并获得尽可能多的食物，同时需要注意在游戏过程中所处的位置，因为不同的位置可以通过传送门到达其他位置，可能会影响食物获取的数量。

# 在游戏开始时，参与者会出发点选择一个方格作为起点，每个方格上至多 22 个传送门，通过传送门可将参与者传送至指定的其它方格。每个方格上都标注了三个数字：id 、 parent-id 和 value 。其中， id 代表方格的编号， parent-id 代表可以通过传送门到达该方格的方格编号， value 代表在该方格获取或失去的食物单位数。

# 参与者需要在地图上行进，到达每个方格并获取或失去对应的食物单位数，直到满足退出游戏的条件之一。参与者的最终得分是所获取食物单位数的总和，需要尽可能地高。

# 需要注意的是地图设计时保证了参与者不可能到达相同的方格两次，并且至少有一个方格的 valuevalue 是正整数，因此，参与者当前所处的方格无传送门，游戏将立即结束。另外，参与者在任意方格上都可以宣布退出游戏，同样会结束游戏。

# 请计算参与者退出游戏后，最多可以获得多少单位的食物。
# 输入描述

# 第一行：方块个数 NN ( N≤10000N≤10000 )

# 接下来 NN 行，每行三个整数 id ， parent-id ， value ，具体含义见题面。

# 0≤id,parent−id<N0≤id,parent−id<N ， −100≤value≤100−100≤value≤100

# 特殊的 parent-id 可以取 −1−1 则表示没有任何方格可以通过传送门传送到此方格，这样的方格在地图中有且仅有一个。
# 输出描述

# 输出为一个整数，表示参与者退出游戏后最多可以获得多少单位的食物。
# 样例
# 样例1

# 输入

# 7
# 0 1 8
# 1 -1 -2
# 2 1 9
# 4 0 -2
# 5 4 3
# 3 0 -3
# 6 2 -3

# 输出

# 9

# 样例解释

# 参与者从方格 00 出发，通过传送门到达方格 44 ，再通过传送门到达方格 55 。一共获得 8+(−2)+3=98+(−2)+3=9 个单位食物，得到食物最多或者参与者在游戏开始时处于方格 22 ，直接主动宣布退出游戏，也可以获得 99 个单位食物。
# 样例2

# 输入

# 3
# 0 -1 3
# 1 0 1
# 2 0 2

# 输出

# 5

# 样例解释

# 参与者从方格 00 出发，通过传送门到达方格 22 ，一共可以获得 3+2=53+2=5 个单位食物，此时得到食物最多。

from collections import *
from math import *
root = -1
n = int(input())
g = defaultdict(list)
food = dict()
for _ in range(n):
    x,p,v = list(map(int,input().split()))
    if p == -1:
        root = x 
    else:
        g[p].append(x)
    food[x] = v  
ans = -inf

def dfs(cur):
    global ans
    s = 0
    for nxt in g[cur]:
        s = max(dfs(nxt),s)
    s += food[cur]
    ans = max(ans,s)
    return s 
dfs(root)
print(ans)