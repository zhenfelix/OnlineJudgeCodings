
# 字节春招后端-2023.03.24-第一题-捡芝麻丢西瓜
# 题目解析以及代码

# 关注公众号:塔子哥学算法，搜索“P1112”即可得到对应题解
# 题目内容

# 我们都知道捡芝麻丢西瓜的故事，现在这个抉择也放到你的面前。有n个西瓜排成一列，每个西瓜有两个属性，用 (weighti,skipi)(weighti​,skipi​) 标识，weightiweighti​表示第i个西瓜的重量（单位斤），skipiskipi​表示捡完第i个西瓜后，就必须跳过接下来的skipiskipi​个西瓜（和捡起的这个挨着的，即 [i+1，skipi+i][i+1，skipi​+i] 的西瓜），不能将它们收入口袋，但是你也可以选择 不捡某个西瓜。而且我们经过每个西瓜的时候都必须做出捡起或者不捡的选择，不能回头。

# 举个例子，给你西瓜＝［［2,2］，［1,1］，［1,1］］：如果西瓜0被捡起了，那么你可以获得2斤的西瓜，但是你不能捡起西瓜1和2。

# 如果你不捡西瓜0，把西瓜1捡起了，你可以得到1斤的西瓜，但是你不能捡起西瓜2了。当然你可以可以跳过西瓜1和2，直接捡西瓜2，那么你获得的也是1斤的西瓜。
# 输入描述

# 首先输入一个 n (1⩽n⩽100000)n (1⩽n⩽100000)代表西瓜的数量

# 然后是 nn 个西瓜的 (weighti,skipi)(weighti​,skipi​)

# (1⩽weighti,skipi⩽100000)(1⩽weighti​,skipi​⩽100000)
# 输出描述

# 输出能捡起西瓜的最大重量
# 样例

# 输入

# 3
# 2 2
# 1 1
# 1 1

# 输出

# 2


from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(n,arr):
    # @lru_cache(None)
    # def dfs(i):
    #     if i >= n: return 0
    #     w, p = arr[i]
    #     return max(dfs(i+1), dfs(i+p+1)+w)
    dp = [0]*(n+1)
    for i in range(n)[::-1]:
        w, p = arr[i]
        dp[i] = max(dp[i+1], w+dp[i+p+1] if i+p+1 < n else w)
    return dp[0]

def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        # n, m, v, w = list(map(int,input().split()))
        n = int(input())
        arr = []
        for _ in range(n):
            arr.append(list(map(int,input().split())))
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        # print(solve(n))
        s = solve(n,arr)
        print(s)
        # m = verify(s)
        # assert(m == n)
        # print(n,s,'ok')
        # print(get_num_without_prize(persons, prizes))
        # print(solve(n,m,vs,ws,cnts))
        # if solve(n,l,r):
        #     print("Yes")
        # else:
        #     print("No")
    # a, b = list(map(int,input().split()))

    # for i in range(1000):
    #     b = randint(1,10000000)
    #     a = randint(1,b)
    #     assert(solve(a,b) == solve_another(a,b))
    #     print(i,a,b,'ok')

if __name__ == "__main__":
    main()