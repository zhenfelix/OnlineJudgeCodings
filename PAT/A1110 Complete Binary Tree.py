import sys, heapq
from collections import *
from functools import cmp_to_key

class Node:
    def __init__(self):
        self.left = None
        self.right = None

# sys.stdin = open('input.txt', 'r')
n = int(input())
ns = [Node() for _ in range(n)]
children = set()
for i in range(n):
    left, right = input().split(' ')
    if left != '-':
        left = int(left)
        ns[i].left = left
        children.add(left)
    if right != '-':
        right = int(right)
        ns[i].right = right
        children.add(right)

roots = [i for i in range(n) if i not in children]
# print([[nn.left,nn.right] for nn in ns],children)
q = roots
res = []

while q:
    # print(q)
    tmp = []
    for root in q:
        res.append(root)
        if root == None: continue
        tmp.append(ns[root].left)
        tmp.append(ns[root].right)
    q = tmp
while res and res[-1] == None: res.pop()
if len(res) > n:
    print('NO',res[0])
else:
    print('YES',res[-1])