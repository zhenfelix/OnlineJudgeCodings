# 参考《数据结构与算法分析》c/c++ 的栈应用部分
# 中缀表达式转换成后缀表达式

# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def __str__(self):
    return (self.left.__str__() if self.left else '')+self.val+(self.right.__str__() if self.right else '')

class Solution:
    def expTree(self, s: str) -> 'Node':
        # Node.__str__ = __str__
        Node.__repr__ = __str__
        # print('test: ', [Node('a'),Node('b')])
        s = '('+s+')'
        ops, st = [], []
        mp = {'(':-1, ')':-1, '-':0, '+':0, '*':1, '/':1}
        for i, ch in enumerate(s):
            if ch not in mp:
                st.append(Node(ch))
            elif ch == '(':
                ops.append(ch)
            else:
                while ops and mp[ch] <= mp[ops[-1]]:
                    op = ops.pop()
                    if op == '(':
                        break
                    root = Node(op)
                    r = st.pop()
                    l = st.pop()
                    root.left, root.right = l, r 
                    st.append(root)
                if ch != ')':
                    ops.append(ch)
            # print(s[:i+1],':',ops,st)
        return st[-1]



# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        # print(s)
        # while s[0] == '(' and s[-1] == ')':
        #     s = s[1:-1]
        n = len(s)
        if n == 1:
            return Node(s)
        left = 0
        for i in range(n)[::-1]:
            ch = s[i]
            if ch in ['-','+'] and left == 0:
                root = Node(ch)
                root.left = self.expTree(s[:i])
                root.right = self.expTree(s[i+1:])
                return root
            if ch == '(':
                left += 1
            if ch == ')':
                left -= 1
        left = 0
        for i in range(n)[::-1]:
            ch = s[i]
            if ch in ['*','/'] and left == 0:
                root = Node(ch)
                root.left = self.expTree(s[:i])
                root.right = self.expTree(s[i+1:])
                return root
            if ch == '(':
                left += 1
            if ch == ')':
                left -= 1
        return self.expTree(s[1:-1])