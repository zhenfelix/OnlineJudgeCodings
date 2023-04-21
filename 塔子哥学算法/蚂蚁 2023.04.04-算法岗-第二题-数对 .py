# 题目内容

# 塔子哥是一名优秀的数据科学家，他经常处理各种数据分析和机器学习问题。最近，他接到了一个新的任务，需要解决一个有趣的问题。

# 这个问题是关于两个数组 AA 和 BB 的。给定两个数组 AA 和 BB，塔子哥需要从中分别选出一个数 aa 和 bb，使得 ∣a−b∣∣a−b∣ 的值在一个给定的区间 [l,r][l,r] 内。

# 他需要计算有多少对满足这个条件的数对。
# 输入描述

# 输入第一行为两个整数 nn ， mm ，分别代表数组 AA 和数组 BB 的长度。

# 第二行为 nn 个整数，第 ii 个整数 aiai​ ；

# 第三行为 mm 个整数，第 ii 个整数 bibi​ 。

# 第四行为两个整数 ll ， rr 。

# 1≤n,m≤1e51≤n,m≤1e5

# 1≤ai,bi≤1e91≤ai​,bi​≤1e9

# 0≤l≤r≤1e90≤l≤r≤1e9
# 输出描述

# 输出为一个整数，代表有多少对满足题目的条件。
# 样例

# 输入

# 4 4
# 1 2 3 4
# 4 3 2 1
# 0 1

# 输出

# 10


from bisect import *
n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
l,r=list(map(int,input().split()))
ans = 0
arr.sort()
brr.sort() 
for a in arr:
    idx = bisect_left(brr,a)
    if idx < m:
        lo = bisect_left(brr,a+l,idx,m) 
        hi = bisect_right(brr,a+r,idx,m) 
        ans += hi-lo 
    if idx >= 0:
        lo = bisect_left(brr,a-r,0,idx)
        hi = bisect_right(brr,a-l,0,idx)
        ans += hi-lo  
print(ans)