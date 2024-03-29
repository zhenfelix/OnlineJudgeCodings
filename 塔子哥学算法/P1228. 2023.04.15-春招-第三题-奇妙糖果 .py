# 题目内容

# 在一个神奇的糖果工厂中，有一种特殊的糖果叫做“奇妙糖果”。这种糖果非常受欢迎，因为它的口感和味道都非常好。

# 奇妙糖果的制作非常复杂，制造过程中要求每种原料的出现次数必须是 kk 的倍数，其中 kk 是一个给定的正整数。

# 在制造奇妙糖果的过程中，制造商们发现，他们可以通过选择不同的原料配方来制造出不同的口感和味道的糖果。他们想要快速计算出可以制造的所有糖果的数量，以便在生产计划中进行参考。

# 为了实现这个目标，他们需要编写一个程序来计算出可以制造的所有奇妙糖果的数量。

# 给定 nn 个原料和正整数 kk，以及每个原料的种类 aiai​ ，你的任务是计算出可以制造的所有的奇妙糖果的数量。

# 注意，这里的“奇妙糖果”是指使用 nn 个原料的任意非空子序列制造出的糖果，其中每种原料的出现次数都是 kk 的倍数。

# 子序列定义是数组中选择若干个元素按照原顺序组成的新数组。
# 输入描述

# 第一行输出为两个整数 n(1≤n≤50)n(1≤n≤50) 和 k(1≤k≤50)k(1≤k≤50) ，表示原料的个数。

# 第二行输出为 nn 个整数，第 ii 个整数为 aiai​ （ 1≤ai≤501≤ai​≤50 ），表示该原料的种类的编号。
# 输出描述

# 输出为一个整数，表示有多少使用 nn 个原料的任意非空子序列制造出的糖果，其中每种原料的出现次数都是 kk 的倍数。
# 样例1

# 输入

# 4 2
# 1 2 1 2

# 输出

# 3

# 说明 三种方案分别为：{1,1}, {2,2}, {1,2,1,2}
# 样例2

# 输入

# 5 2
# 1 2 1 2 1

# 输出

# 7

# 说明 七种方案分别为：{1,0,1,0,0}, {1,0,0,0,1}, {0,0,1,0,1}, {0,2,0,2,0}, {1,2,1,2,0}, {0,2,1,2,1}, {1,2,0,2,1} (0代表不选对应位置的原料)

from math import comb 
from collections import *

n, k = list(map(int,input().split()))
arr = list(map(int,input().split()))
cc = Counter(arr)
ans = 1
for _, v in cc.items():
    ans *= sum(comb(v,i) for i in range(0,v+1,k))
print(ans-1)
