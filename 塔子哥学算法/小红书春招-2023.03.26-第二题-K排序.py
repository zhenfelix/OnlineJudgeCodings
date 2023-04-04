
# 小红书春招-2023.03.26-第二题-K排序
# 题目内容

# 在算法中，有各种各样的排序算洁，例如归并排序，冒排序，快速排序等等、本题中，我们合使用一种断的排序算法：K排序。

# K排序算法描述如下：首先，算法需要按某种规则选择该数列上至多K个位置，将其对应的数抽出来，其他的数都往左对齐，之后这K个数排好序之后依次放在原数列未尾，以上过程算作一次操作。

# 例如，对于数列 [1.3.5,4,2]，当K＝2时可以选样数字5和4，之后数列变成[1,3,2.4,5].

# 你的任务是：对于给定的数判，你需要计算出最少需要多少次上述操作，使得整个数列从小到大排好序？
# 输入描述

# 第一行一个正整数T，表示有T组数据。

# 对于每一数据，第一行输入两个正整数n,k;；第二行输入n个数 a1,a2,…,ana1​,a2​,…,an​, 该序列是一个 1~n 的排列。

# 对于所有数据：1⩽k⩽n⩽105,1⩽at⩽n,ai≠aj,1⩽T⩽51⩽k⩽n⩽105,1⩽at​⩽n,ai​=aj​,1⩽T⩽5
# 输出描述

# 对于每一组数据，输出一行一个整数，表示答案。
# 样例

# 输入

# 2
# 5 1
# 1 2 3 4 5
# 5 2
# 1 3 5 4 2

# 输出

# 0
# 2

# 样例解释

# 第一组数据，原数列已经排好序，则无需进行任何操作；

# 第二组数据，操作如下：

# [1,3,5,4,2] -> [1,5,4,2,3]

# [1,5,4,2,3] -> [1,2,3,4,5]


from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *
from string import *

def solve(n,k,arr):
    cur = 0
    for a in arr:
        if a == cur+1:
            cur += 1
    return (n-cur-1)//k+1


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    case = int(input())
    for _ in range(case):
        n, k = list(map(int,input().split()))
        # n = int(input())
        arr = list(map(int,input().split()))
        # brr = list(map(int,input().split()))
        # s = input()
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        print(solve(n,k,arr))
        

if __name__ == "__main__":
    main()