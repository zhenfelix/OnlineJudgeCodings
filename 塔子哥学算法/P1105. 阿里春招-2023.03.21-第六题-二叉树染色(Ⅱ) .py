
# 阿里春招-2023.03.21-第六题-二叉树染色(Ⅱ)
# 题目内容

# 给定一个 nn 层的满二叉树，一共 2n−12n−1 个节点，编号从 11 到 2n−12n−1 。

# 对于编号为 ii （ 1≤i≤2n−1−11≤i≤2n−1−1 ）的节点，它的左儿子为 2i2i ，它的右儿子为 2i+12i+1 。有 qq 次操作，每次操作我们选择一个节点，将该节点的子树的所有节点全部染红。

# 每次操作后，你需要输出当前二叉树红色节点的数量。

# 我们定义一棵二叉树是满二叉树，当且仅当每一层的节点数量都达到了最大值 （即无法在这一层添加新节点）。
# 输入描述

# 第一行输入两个正整数 nn 和 qq ，代表二叉树的层数和操作次数。

# 接下来的 qq 行，每行输入一个正整数 aiai​ ，代表染色的节点编号。

# 1≤n≤401≤n≤40

# 1≤q≤100001≤q≤10000

# 1≤ai≤2n1≤ai​≤2n
# 输出描述

# 输出 qq 行，每行输入一个正整数，代表当前操作结束后二叉树的红色节点数量。
# 样例

# 输入

# 2 3
# 2
# 1
# 3

# 输出

# 1
# 3
# 3



from random import *
import sys
from collections import * 
from math import * 

def solve():
    # sys.stdin = open('contests/input', 'r')
    n, q = list(map(int,input().split()))
    color = set()
    # arr = list(map(int,input().split()))
    def check(t):
        cnt = 0
        while t:
            if t in color: return 0
            cnt += 1
            t >>= 1
        return (1<<(n+1-cnt))-1
    cc = Counter()
    for _ in range(q):
        a = int(input())
        delta = max(check(a)-cc[a], 0)
        color.add(a)
        while a:
            cc[a] += delta
            a >>= 1
        print(cc[1])
    return 

solve()