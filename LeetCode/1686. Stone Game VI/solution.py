class Solution:
    def stoneGameVI(self, A, B):
        A = sorted(zip(A, B), key=sum)
        return cmp(sum(a for a, b in A[::-2]), sum(b for a, b in A[-2::-2]))