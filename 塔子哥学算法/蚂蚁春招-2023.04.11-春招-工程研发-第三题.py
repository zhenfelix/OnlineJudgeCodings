# 题目内容

# 曾经有一个名叫塔子哥的年轻人，他热衷于解决各种复杂的问题。有一天，他在某个二手市场上意外地发现了一排格子，每个格子的背景颜色要么是红色，要么是蓝色。这些格子排成一排，让人感觉像是一个秘密代码。

# 塔子哥好奇地观察了一会儿，然后他突然想到了一个有趣的问题：如果在每个格子上填写一个小写字母，那么相同的字母应该出现在相同的背景颜色中。这听起来似乎很简单，但实际上这是一个复杂的问题，需要精心计划和良好的逻辑。

# 然后，塔子哥只关注出现次数最多的字母，他希望尽可能降低它的出现次数。他开始思考并探索这个问题的解决方案，你可以帮助塔子哥解决这个问题吗？
# 输入描述

# 一个仅由字符 '0' 和 '1 ' 组成的字符串，长度不超过 200000200000 。

# 字符串用于表示塔子哥拿到的格子的颜色。第 ii 个字符为 '0' 代表第第 ii 个格子为蓝色背景，字符 '1' 代表红色背景。
# 输出描述

# 一个仅由小写字母构成的字符串，第i个字符为第1个格子上填写的字母，请务必保证字符串是合法的。如果有多解，输出任意即可.
# 样例
# 样例一

# 输入

# 10101011

# 输出

# abcdefgh

# 样例二

# 输入

# 11111111111111111000000000000000000000

# 输出

# aabbccddeeffgghhijjkkllmmnnooppqqrrsst

#     在题库中打开

# 春招模拟赛第六场|Ant|2023.04.11研发岗笔试
# 已参加

#     查看比赛
#     成绩表
#     讨论
#     所有递交
#     帮助

# 状态
#     已结束 (已参加) 
# 规则
#     IOI
# 题目
#     3
# 开始于
#     2023-4-16 19:15 
# 结束于
#     2023-4-16 20:20 
# 持续时间
#     1.3 小时
# 主持人
#     luti 
# 参赛人数
#     91



from math import * 
from string import * 
s=input()
cc=[0]*2
for ch in s:
    cc[int(ch)] += 1
ans = [-1,-1,inf]
for x in range(27):
    y = 26-x 
    if x == 0 or cc[0] == 0:
        if x != cc[0]: continue
    if y == 0 or cc[1] == 0:
        if y != cc[1]: continue
    cnt = 0
    if x > 0:
        cnt = max(cnt, (cc[0]-1+x)//x)
    if y > 0:
        cnt = max(cnt, (cc[1]-1+y)//y)
    if cnt < ans[-1]:
        ans = [x,y,cnt]
n = len(s)
x = ans[0]
candidates = [ascii_lowercase[:x],ascii_lowercase[x:]]
idx = [0]*2 
res = []
for ch in s:
    ch = int(ch)
    i = idx[ch]
    sz = len(candidates[ch])
    res.append(candidates[ch][i%sz])
    idx[ch] += 1
print(''.join(res))