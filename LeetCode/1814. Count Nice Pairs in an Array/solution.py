class Solution:
    def countNicePairs(self, A):
        res = 0
        count = collections.Counter()
        for a in A:
            b = int(str(a)[::-1])
            res += count[a - b]
            count[a - b] += 1
        return res % (10**9 + 7)        