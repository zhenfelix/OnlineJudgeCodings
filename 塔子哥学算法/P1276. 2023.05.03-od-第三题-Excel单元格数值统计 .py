
# 2023.05.03-od-第三题-Excel单元格数值统计
# 题目描述

# 有一天塔子哥去朋友家玩，发现朋友的弟弟在玩一个有趣的棋盘。

# 这个棋盘上是按类似于国际象棋的方法来标记的，从左到右依次为A~G，从上到下是数字，每个格子都可以用 字母+数字 来表示，如图：
#     A   B   C
# 1   A1  B1  C1
# 2   A2  B2  C2
# 3   A3  B3  C3

# 棋盘上被朋友的弟弟写满一些数字和公式，塔子哥检查整个棋盘发现：

#     每个格子中只写了两种内容，数字或公式；

#     格子里的数字全是非负整数，例如 33 、7777 ；

#     格子里的公式固定以=开头，仅包含下面三种情况：

#     （1）等于另外某个格子的值，例如=B12；

#     （2）等于另外两个格子的加减运算 (仅为+或-),例如=C1-C2、=C3+B2；

#     （3）等于其它格子和数字的加减运算(仅为+或-),例如=B1+1、=100-B2；

# 塔子哥十分好奇，通过询问，他明白了这个棋盘的作用。两个人提前将棋盘写满，一个人指定棋盘上的某个矩形，另一个人快速计算这个矩形范围中所有格子的和。谁的用时短谁就赢。

# 塔子哥觉得这个游戏很有意思，就想在电脑上把它复刻出来。

# 为了保证游戏的正常运行，塔子哥为游戏添加了这些限制：

# 1.公式内容都是合法的,保证没有错误，例如不存在=C+1、=C1-C2+B3,=5、=3+5； 2.不会出现循环引用,例如当 A1A1 位置是=B1+C1、C1C1 位置上是=A1+B2时，这是非法的；

# 现在塔子哥生成了一个游戏棋盘，他想找人测试一下这个游戏，于是他找到了你。
# 输入描述

# 第一行两个整数 NN , MM ( 1≤N≤301≤N≤30,1≤M≤261≤M≤26),表示给定棋盘区域的行数和列数,。

# 接下来 NN 行，每行 MM 个以空格分隔的字符串，表示给定棋盘的单元格内容。

# 最后一行输入的字符串，表示给定的矩形范围，形如A1：C2，冒号左边表示矩形左上角的棋盘格，冒号右边表示矩形右下角的棋盘格。

# 输入保证合法。
# 输出描述

# 一个整数sum,表示给定矩形范围中所有格子所代表的值的累加总和

# 范围是 −2,147,483,648≤sum≤2,147,483,648−2,147,483,648≤sum≤2,147,483,648。
# 样例1

# 输入

# 3 3
# =9+B1 =3+B2 =A2+A3
# =C2-8 =C3+C3 =C3
# =B3+B3 =C3 12
# B3:C3

# 输出

# 24

# 棋盘情况:

# 36 27 28

# 4 24 12

# 24 12 12
# 样例2

# 输入

# 3 3
# =86-A2 =43+A2 =B2+99
# =C3+B2 =C2+88 =A3-66
# =B3 9 97
# B1:B2

# 输出

# 202

# 棋盘情况:

# -42 171 130

# 128 31 -57

# 9 9 97


from functools import *
from string import *
n, m = list(map(int,input().split()))
arr = []
for _ in range(n):
    line = input().split()
    arr.append(line) 
mat = [[0]*(m+1) for _ in range(n+1)]
# print(arr)

def calc(s):
    c, r = ord(s[0])-ord('A'), int(s[1:])-1
    return r, c 

@lru_cache(None)
def parse(s):
    # print(s)
    if all(ch not in ascii_uppercase for ch in s):
        return int(s)
    c, r = ord(s[0])-ord('A'), int(s[1:])-1
    return dfs(r,c)

@lru_cache(None)
def dfs(i,j):
    # print(i,j)
    s = arr[i][j]
    if s[0] == '=':
        s = s[1:]
        if '+' in s:
            a, b = s.split('+')
            return parse(a)+parse(b)
        elif '-' in s:
            a, b = s.split('-') 
            return parse(a)-parse(b)
        else:
            return parse(s) 
    return int(s)

for i in range(n):
    for j in range(m):
        mat[i+1][j+1] = mat[i+1][j]+mat[i][j+1]-mat[i][j]+dfs(i,j)

a,b = input().split(':')
ra,ca = calc(a) 
rb,cb = calc(b)
print(mat[rb+1][cb+1]+mat[ra][ca]-mat[rb+1][ca]-mat[ra][cb+1])