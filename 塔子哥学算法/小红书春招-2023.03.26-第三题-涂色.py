
# 小红书春招-2023.03.26-第三题-涂色
# 题目内容

# 给出一个数组，你需要求出按顺序对其进行一系区间操作后终所得的数组。

# 操作有三种

# 1.将下标在L到R之间的元素全部或上X。

# 2.将下标在L到R之间的元素全部与上X。

# 3.将下标在L到R之间的元素全部设为X。
# 输入描述

# 第一行有一个正整数 N(1⩽N⩽100000)N(1⩽N⩽100000)，代表数组的长度。

# 第二行有 NN 个非负整数，范围在00到 220−1220−1之间，代表数组中的元素。

# 第三行有一个正整数M（1⩽M⩽1000001⩽M⩽100000），代表操作次数。

# 第四行有M个正整数，代表M次操作中的区间左端点L。

# 第五行有M个正整数，代表M次操作中的区间右通点R。

# 第六行是一个长度为M的字符串，'|' 代表操作1，'&' 代表操作2。'=' 代表操作3。

# 第七行有M个正整数，代表M次操作中的参数X.
# 输出描述

# 在一行中输出N个数，代表所有操作按顺序完成后最终所得的数据。
# 样例

# 输入

# 4
# 5 4 7 4
# 4
# 1 2 3 2
# 4 3 4 2
# =|&=
# 8 3 6 2

# 输出

# 8 2 2 0


from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *
from string import *

def solve(n,arr,m,left,right,ops,values):
    bmax = 21
    ans = [0]*n 
    for b in range(bmax):
        push, pop, hq = [[] for _ in range(n+1)], [[] for _ in range(n+1)], []
        inqueue = [0]*(n+m)
        for i in range(n):
            v = (arr[i]>>b)&1
            push[i].append((inf,v,i))
            pop[i+1].append((inf,v,i))
        for i in range(m):
            l, r, op, v = left[i]-1, right[i]-1, ops[i], values[i]
            if (op == '=' and (v>>b)&1) or (op == '|' and (v>>b)&1):
                push[l].append((-i,1,i+n))
                pop[r+1].append((-i,1,i+n))
            elif (op == '=' and ((v>>b)&1 == 0)) or (op == '&' and ((v>>b)&1 == 0)):
                push[l].append((-i,0,i+n))
                pop[r+1].append((-i,0,i+n))
        for i in range(n):
            for t, v, j in push[i]:
                heappush(hq,(t,v,j))
                inqueue[j] = 1
            for t, v, j in pop[i]:
                inqueue[j] = 0
            while hq and not inqueue[hq[0][-1]]:
                heappop(hq)
            v = 0
            if hq and hq[0][1]: v = 1
            if v: ans[i] |= (1<<b)
    # print(*ans)

    return ans 


def brute(n,arr,m,left,right,ops,values):
    for i in range(m):
        l, r, op, v = left[i]-1, right[i]-1, ops[i], values[i]
        for j in range(l,r+1):
            if op == '=':
                arr[j] = v
            elif op == '&':
                arr[j] &= v 
            else:
                arr[j] |= v 
    return arr 

def generate():
    n = randint(10,1000)
    arr = [randint(1,1<<19) for _ in range(n)]
    m = randint(10,1000)
    left, right, ops, values = [], [], [], []
    for _ in range(m):
        left.append(randint(1,n))
        right.append(randint(left[-1],n))
        ops.append(choice("|&="))
        values.append(randint(1,1<<19))
    return n,arr,m,left,right,''.join(ops),values




def main():
    sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for i in range(10):
        # n, k = list(map(int,input().split()))
        n = int(input())
        arr = list(map(int,input().split()))
        m = int(input())
        left = list(map(int,input().split()))
        right = list(map(int,input().split()))
        ops = input()
        values = list(map(int,input().split()))
        # brr = list(map(int,input().split()))
        # s = input()
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        # n,arr,m,left,right,ops,values = generate()
        # solve(n,arr,m,left,right,ops,values)
        ans1 = solve(n,arr,m,left,right,ops,values)
        ans2 = brute(n,arr,m,left,right,ops,values)
        assert(ans1 == ans2)
        print(f"{i}th test case ok")
        # print(solve(n,arr,m,left,right,ops,values))
        

if __name__ == "__main__":
    main()