
# 2023.4.2-网易有道研发岗-第二题-编码序列化存储
# 题目内容

# 二叉树按以下规则进行字符串编码序列化存储：

#     如果当前树为空，则表示为X;
#     如果当前树不为空，则表示为(left_sub_tree)current_value(right_sub_tree);
#         left_sub_tree:左子树按此规则序列化后得到的字符串
#         right sub_tree:右子树按此规则序列化后得到的字符串

# 请编写代码实现从输入的字符串反序列化出对应的二叉树结构，并输出 所有结点的 深度*权值 之和. 根的深度定义为1
# 输入描述

# 输入字符串编码的二叉树
# 输出描述

# 深度*权值之和
# 示例1

# 输入

# ((X)2(X))1(((X)4(X))3((X)2(X)))

# 输出

# 29

# 说明

# 字符串长度不超过100000100000.保证给定的字符串形成一个合法的二叉树。

# 1≤current_value≤100001≤current_value≤10000

s = input()
ans = 0
d = 1
num = ''
for ch in s:
    if ch == '(':
        if num:
            ans += d*int(num)
            num = ''
        d += 1
    elif ch == ')':
        d -= 1
    elif ch == 'X':
        continue
    else:
        num += ch  
print(ans)