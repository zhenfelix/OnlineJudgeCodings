class Solution:
    def minNumberOperations(self, A):
        res = pre = 0
        for a in A:
            res += max(a - pre, 0)
            pre = a
        return res        