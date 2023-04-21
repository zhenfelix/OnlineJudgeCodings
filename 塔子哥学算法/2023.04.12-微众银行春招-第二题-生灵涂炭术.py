# 题目描述：

# 大魔法师塔子哥有一个成名绝招，名为生灵涂炭术。该禁咒所到之处寸草不生，万物归 00 ，但是塔子哥一生可以使用的次数只有三次。

# 在塔子哥的世界里充斥着正负两种能量，正能量对人体有益，而负能量对人体是有害的。

# 已知地图上有 nn 个排成一列的地域，每个地域的能量都不一样，可以用一个数字来代表某个地域中正负能量的总数，正数代表正能量比负能量多，反之亦然。

# 塔子哥在他的前半生使用了一次生灵涂炭术，现在他能使用生灵涂炭术的次数只剩下了两次，现在塔子哥可以对任何一个连续的区域使用生灵涂炭术，使用之后，无论该连续区域中能量有多少，都会清0。

# 塔子哥希望天地间的正能量最多，他想知道在他使用了技能以后能使得天地间的正能量最多为多少？（如果天地间都是正能量，不使用技能也是可以的）
# 输入描述

# 输入第一行仅包含一个正整数 nn ( 1≤n≤1000001≤n≤100000 )，表示地域数量。

# 输入第二行包含 nn 个整数，每个整数代表一个地域的能量总和,保证这个数值的绝对值不大于 100000100000 。
# 输出描述

# 输出仅包含一个整数，即正能量最多为多少。
# 样例

# 输入

# 5
# 5 -10 6 1 -5

# 输出

# 12

# 样例解释

# 显然把 {−10}{−10} 和 {−5}{−5} 删掉之后，余下的和为 1212 。

from math import *
n=int(input())
arr=list(map(int,input().split()))
left = [0]*n 
cur = 0
mx = 0
for i in range(n):
    cur += arr[i]
    mx = max(mx,cur)
    left[i] = mx 
right = [0]*n 
cur = 0
mx = 0
for i in range(n)[::-1]:
    cur += arr[i]
    mx = max(mx,cur)
    right[i] = mx 
ans = max(left[-1],right[0])
for i in range(n-1):
    ans = max(ans,left[i]+right[i+1])
cur = 0
for i in range(n):
    cur += arr[i]
    left[i] -= cur 
cur = 0
mx = -inf
for i in range(n-1):
    cur += arr[i]
    mx = max(mx,left[i])
    ans = max(ans,cur+mx+right[i+1])
print(ans)