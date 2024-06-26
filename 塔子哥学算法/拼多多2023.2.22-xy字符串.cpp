
// 2023.2.22-xy字符串
// 题目内容

// 塔子哥是一名计算机科学家，他正在研究一种特殊的字符串。这个字符串由小写字母 ‘x’ 和特殊字符 ‘*’ 构成。现在，他想要将这个字符串中的每个字符 ‘*’ 替换成 00 到 mm 个小写字母 ‘y’ ，并将替换后的字符串称为 "xy字符串" 。对于原始字符串 ss ，可以用不同替换方式可以得到多种不相同的 "xy字符串" ，塔子哥现在想知道第 nn 小的 "xy字符串” ，但是他现在忙于研究 "xy字符串” 的其他性质，你帮他解决这个问题吗？

// 假定有两个 ”xy字符串” 分别为 s1s1 、 s2s2 ，这两个 “xy字符串” 满足以下特性：

//     如果 s1s1 和 s2s2 的长度不同，或者下标对应的字母不同，则认为 s1s1 和 s2s2 不相同
//     如果 s1s1 要小于 s2s2 的话，需要满足任意条件之一
//         s1s1 是 s2s2 的前缀且 s1s1 与 s2s2 不相同
//         比较 s1s1 和 s2s2 ，从左往右第个字母不同， 且 s1s1 的字母小于 s2s2 的字母

// 输入描述

// 第一行输入一个数字 TT ( 1≤T≤25001≤T≤2500 ) ，表示有工组测试用例。对于每一组用例：

// 第一行分别有 33 个数字， ll ( 1≤1≤25001≤1≤2500 ) ， mm ( 0≤m≤25000≤m≤2500 )， nn ( 1≤n≤10181≤n≤1018 )。

// 第二行有一个字符串 ss 由 ll 个字符构成，字符串由小写字母 'x' 和特殊字符 ‘*’ 构成。
// 输出描述

// 对于每组测试用例，输出一行字符串，表示第 nn 小的 "xy字符串”
// 样例
// 样例一：

// 输入

// 2
// 4 1 3
// x**x
// 2 4 3
// x*

// 输出

// xyyx
// xyy

// 备注

// TT 组测试用例的字符串 ll 加起来不会超过 25002500 。对于每组测试用例，可以保证 nn 不会超过 不相同的 "xy字符串" 的数量

import sys 

# sys.stdin = open("contests/input","r")
t = int(input())

for _ in range(t):
    n, m, rank = list(map(int,input().split()))
    rank -= 1
    s = input()
    arr = []
    pre = ''
    for ch in s:
        if ch != pre:
            arr.append('')
        arr[-1] += ch 
        pre = ch 

    sz = len(arr)
    for i in range(sz)[::-1]:
        if arr[i][0] == 'x': continue
        cnt = m*len(arr[i])+1
        arr[i] = 'y'*(rank%cnt)
        rank //= cnt 
    
    print(''.join(arr))
