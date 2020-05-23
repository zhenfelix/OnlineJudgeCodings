import sys, heapq
from collections import *
from functools import cmp_to_key

class Node:
    def __init__(self,v):
        self.val = v
        self.left, self.right = None, None


def main():
    def dfs(cur, depth):
        nonlocal mx
        if cur == None: return
        cnt[depth] += 1
        mx = max(mx, depth)
        dfs(cur.left, depth + 1)
        dfs(cur.right, depth + 1)
        return

    def build(cur, val):
        if cur == None:
            cur = Node(val)
            return cur
        if val <= cur.val:
            cur.left = build(cur.left, val)
        else:
            cur.right = build(cur.right, val)
        return cur
    # sys.stdin = open('input.txt', 'r')
    n = int(input())
    arr = map(int, input().split(' '))
    cnt = defaultdict(int)
    mx = 0
    root = None
    for a in arr:
        root = build(root, a)
    dfs(root, 0)
    print("{} + {} = {}".format(cnt[mx], cnt[mx - 1], cnt[mx] + cnt[mx - 1]))

if __name__ == "__main__":
    main()