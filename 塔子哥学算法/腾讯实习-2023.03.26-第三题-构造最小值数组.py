
# 腾讯实习-2023.03.26-第三题-构造最小值数组
# 题目内容

# 给定2个整数数组A，B，数组长度都为N，数组B为权值数组，权值数据范围为[0,2][0,2]，请你构造一个数组C，满足以下条件:

# 1.长度为N

# 2.数组元素范围为[1,N][1,N]，且元素值不能重复,即为N的一个排列

# 3.若bi>bjbi​>bj​ 那么一定保证 ci>cjci​>cj​

# 4.数组C与数组A每个元素之差的和的绝对值最小，即x=∑i=1n∣Ci−Ai∣x=∑i=1n​∣Ci​−Ai​∣, xx 最小

# 请你输出这个 xx 的最小值
# 输入描述

# 第一行输入一个整数N

# 第二行输入N个正整数，每个数代表数组A的元素

# 第三行输入N个整数，每个数代表数字B的元素，范围为[0，2]

# 1⩽N⩽2∗1051⩽N⩽2∗105

# 1⩽A[i]⩽1091⩽A[i]⩽109

# 0⩽B[i]⩽20⩽B[i]⩽2
# 输出描述

# 输出x=∑i=1n∣Ci−Ai∣x=∑i=1n​∣Ci​−Ai​∣的最小值
# 样例
# 样例1

# 输入

# 2
# 1 10
# 1 0

# 输出

# 10

# 样例解释

# 当 i=0,j=1i=0,j=1 时，i<ji<j，B[i]=1>B[j]=0B[i]=1>B[j]=0，所以只能为

# C[i]=2,C[j]=1C[i]=2,C[j]=1，故∣1−2∣+∣10−1∣=10，x=10∣1−2∣+∣10−1∣=10，x=10
# 样例2

# 输入

# 4
# 2 1 4 2
# 2 2 2 2

# 输出

# 1

# 样例解释

# C 数组可以为2 1 4 3，故x=1
# 样例3

# 输入

# 6
# 100 2 3 1 5 6
# 0 1 2 0 2 1

# 输出

# 104


from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *



def solve(n,arr,brr):
    idx = list(range(n))
    idx.sort(key = lambda x: (brr[x],arr[x]))
    ans = 0
    for i in range(n):
        j = idx[i]
        ans += abs(i+1-arr[j])
    return ans 


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        # n, k = list(map(int,input().split()))
        n = int(input())
        arr = list(map(int,input().split()))
        brr = list(map(int,input().split()))
        # s = input()
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        print(solve(n,arr,brr))
        

if __name__ == "__main__":
    main()