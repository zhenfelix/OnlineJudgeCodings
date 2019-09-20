from typing import List


import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 0

class AVLtree:
    def __init__(self):
        self.root = None

    def height(self, cur):
        if not cur:
            return -1
        return cur.height

    def insert(self, cur, val):
        if not cur:
            cur = TreeNode(val)

        else:
            if val < cur.val:
                cur.left = self.insert(cur.left, val)
                if self.height(cur.left) - self.height(cur.right) == 2:
                    if val < cur.left.val:
                        cur = self.SingleRotateLeft(cur)
                    else:
                        cur = self.DoubleRotateLeft(cur)
            else:
                cur.right = self.insert(cur.right, val)
                if self.height(cur.right) - self.height(cur.left) == 2:
                    if val >= cur.right.val:
                        cur = self.SingleRotateRight(cur)
                    else:
                        cur = self.DoubleRotateRight(cur)

        cur.height = max(self.height(cur.left), self.height(cur.right)) + 1
        return cur

    def SingleRotateLeft(self, cur):
        left = cur.left
        cur.left = left.right
        left.right = cur
        cur.height = max(self.height(cur.left), self.height(cur.right)) + 1
        left.height = max(self.height(left.left), self.height(left.right)) + 1
        return left

    def SingleRotateRight(self, cur):
        right = cur.right
        cur.right = right.left
        right.left = cur
        cur.height = max(self.height(cur.right), self.height(cur.left)) + 1
        right.height = max(self.height(right.right), self.height(right.left)) + 1
        return right

    def DoubleRotateLeft(self, cur):
        cur.left = self.SingleRotateRight(cur.left)
        return self.SingleRotateLeft(cur)

    def DoubleRotateRight(self, cur):
        cur.right = self.SingleRotateLeft(cur.right)
        return self.SingleRotateRight(cur)





class Solution:
    def findRoot(self, arr):
        T = AVLtree()
        for val in arr:
            T.root = T.insert(T.root, val)
        return T.root.val



if __name__ == "__main__":

    # sys.stdin = open('input.txt', 'r')
    N = int(input())
    arr = list(map(int, input().split(' ')))
    # print(N)
    # print(arr)
    Sol = Solution()

    print(Sol.findRoot(arr))