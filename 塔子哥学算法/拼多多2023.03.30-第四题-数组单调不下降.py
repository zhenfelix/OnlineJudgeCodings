
# 2023.03.30-第四题-数组单调不下降
# 题目内容

# 曾经有一个塔子哥，他是一个热爱数学的年轻人，他喜欢思考数学问题，研究各种算法。

# 有一天，他遇到了一个非常有趣的问题。他的朋友给了他一个长度为 nn 的数组 aa，让他通过一系列的操作使得数组单调不下降，也就是说，对于任意的 ii 和 jj，如果 i≤ji≤j，那么 ai≤ajai​≤aj​。

# 在听到这个问题的时候，塔子哥很兴奋，因为他知道这个问题可以用他最擅长的算法来解决。他想到了一种方法，可以通过将数组中某些数变成 00 的方式来达到目标。具体地说，他可以选择数组中的一个数 xx，然后将所有等于 xx 的数都变成 00。这样做可以让某些数“消失”，也就是让它们不再影响数组单调不下降的性质。但是，这个方法有一个缺点，就是它需要重复执行很多次，才能让整个数组单调不下降。

# 塔子哥觉得这个问题非常有趣，于是决定尝试解决它。他开始思考如何通过最少的操作次数，使得整个数组单调不下降。

# 有 tt 组输入。
# 输入描述

# 输入第一行为一个整数 tt ，代表 tt 组输入。（ 1≤t≤1001≤t≤100 ）

# 每一组输入，第一行为一个整数 nn 。

# 第二行为 nn 个整数。

# （ 1≤n,ai≤1041≤n,ai​≤104 ）
# 输出描述

# 输出最小的操作次数。
# 样例

# 输入

# 3
# 3
# 5 1 5
# 5
# 1 1 2 2 2
# 3
# 1 4 1

# 输出

# 2
# 0
# 2


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    st = []
    seen = set()
    for a in arr:
        if a in seen:
            a = 0
        if st and st[-1] > a:
            for b in st:
                seen.add(b)
            st = []
        if a and a not in seen:
            st.append(a)
    print(len(seen))

from math import *
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    m = len(set(arr))
    ans = m
    nxt = inf
    mp = dict()
    seen = set()
    for i, v in enumerate(arr):
        if v not in mp:
            mp[v] = i 
    mp[inf] = n 
    for i in range(n)[::-1]:
        seen.add(arr[i])
        if arr[i] > nxt:
            break
        if arr[i] < nxt and mp[nxt] < i:
            break 
        if mp[arr[i]] == i:
            ans = min(ans,m-len(seen))
        
        nxt = arr[i]

    print(ans)